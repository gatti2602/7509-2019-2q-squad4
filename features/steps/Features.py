from behave import *

use_step_matcher("re")


@given("que soy gerente de Marketing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given que soy gerente de Marketing')


@when("quiero ver los features que se estan creando en el sistema")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When quiero ver los features que se estan creando en el sistema')


@then("el sistema me muestra una lista de todos los features con su estado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema me muestra una lista de todos los features con su estado')