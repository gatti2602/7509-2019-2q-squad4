from behave import *
from producto.models import Feature
from datetime import datetime as dt


@given("que hay features en el sistema")
def step_impl(context):
    if Feature.objects.count() == 0:
        feature = Feature(description="Feat1", expected_delivery=dt.now(), status="PENDIENTE")
        feature.save()

@when("indico al sistema que muestre los features")
def step_impl(context):
    context.features = Feature.objects.all()


@then("obtengo una lista de todos los features en desarrollo")
def step_impl(context):
    assert len(context.features) > 0


@given("que ingreso a la pagina de carga de features")
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/producto/feature/new')

@when("completo los valores description, expected_date y status")
def step_impl(context):
    context.description = context.driver.find_element_by_name('description')
    context.status = context.driver.find_element_by_name('status')
    context.expected_Date = context.driver.find_element_by_name('expected_date')
    assert context.description is not None
    assert context.status is not None
    assert context.expected_Date is not None
    context.description.send_keys('New Feature')
    context.status.send_keys('APROBADA')
    context.expected_Date.send_keys('2019-01-01')
    context.expected_Date.submit()


@then("el feature se crea en el sistema")
def step_impl(context):
    assert Feature.objects.filter(description='New Feature').count() == 1

