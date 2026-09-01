# conftest.py
# pip install allure-pytest allure-python-commons
import pytest
import allure
from pytest_bdd.parser import Feature, Scenario, Step


SEVERITY_MAP = {
    'blocker': allure.severity_level.BLOCKER,
    'critical': allure.severity_level.CRITICAL,
    'high': allure.severity_level.CRITICAL,
    'normal': allure.severity_level.NORMAL,
    'low': allure.severity_level.MINOR,
    'minor': allure.severity_level.MINOR,
    'trivial': allure.severity_level.TRIVIAL,
}

@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_before_step(request, step, scenario, feature):
    '''Creates an Allure step from the BDD step text.'''
    allure.step(f'{step.keyword} {step.name}')
    yield

@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(request, step, scenario, feature):
    '''Closes the current Allure step after execution.'''
    yield

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_step_error(request, step, scenario, feature, exception):
    '''Attaches the step error text to the Allure report.'''
    allure.attach(
        f'Error in step: {step.keyword} {step.name}\n'
        f'Exception: {str(exception)}',
        name='Step Error',
        attachment_type=allure.attachment_type.TEXT
    )

def pytest_collection_modifyitems(session, config, items):
    '''Automatically applies Allure metadata based on tags and the .feature file structure.'''
    for item in items:
        # Gets the associated scenario from pytest-bdd
        scenario = getattr(item, '_pytest_bdd_scenario', None)
        if not scenario:
            continue

        feature: Feature = scenario.feature

        allure.dynamic.feature(feature.name)
        allure.dynamic.story(scenario.name)
        allure.dynamic.title(scenario.name)
        if feature.description:
            allure.dynamic.description(feature.description.strip())

        all_tags = set(feature.tags) | set(scenario.tags)

        for tag in all_tags:
            tag_lower = tag.lower()

            if tag_lower in SEVERITY_MAP:
                allure.dynamic.severity(SEVERITY_MAP[tag_lower])

            if tag_lower in ('smoke', 'regress', 'sanity', 'e2e'):
                allure.dynamic.label('layer', tag_lower)
