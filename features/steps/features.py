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