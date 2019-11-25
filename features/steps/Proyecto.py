from datetime import datetime, timedelta

from behave import *

from proyecto.models import Proyecto, RiesgoImpacto

use_step_matcher("re")


@given("que estoy viendo el detalle del proyecto")
def step_impl(context):
    # Crear RiesgoImpacto
    riesgo_i = RiesgoImpacto(descripcion='Bajo', impacto=0.1)
    riesgo_i.save()

    context.proyecto = Proyecto(titulo="Test Project",
                                descripcion="Test Project",
                                fecha_inicio_real=datetime.now(),
                                fecha_fin_real=datetime.now() + timedelta(1.0))
    context.proyecto.save()
    context.proyecto.CrearRiesgo("Test Risk", 0.1, riesgo_i)

    url = context.get_url('proyecto:project_detail', context.proyecto.cod_proyecto)
    assert url is not None
    context.driver.get(url)


@when("voy a la seccion de Riesgos")
def step_impl(context):
    pass


@then("el sistema lista todos los riesgos")
def step_impl(context):
    tag = context.driver.find_element_by_link_text("Test Risk")
    assert tag is not None


@given("que deseo agregar un nuevo riesgo")
def step_impl(context):
    # Crear RiesgoImpacto
    riesgo_i = RiesgoImpacto(descripcion='Bajo', impacto=0.1)
    riesgo_i.save()

    context.proyecto = Proyecto(titulo="Test Project",
                                descripcion="Test Project",
                                fecha_inicio_real=datetime.now(),
                                fecha_fin_real=datetime.now() + timedelta(1.0))
    context.proyecto.save()
    url = context.get_url('proyecto:project_detail', context.proyecto.cod_proyecto)
    assert url is not None
    context.driver.get(url)


@when("ingreso a la seccion riesgo y voy a agregar uno nuevo")
def step_impl(context):
    tag = context.driver.find_element_by_link_text("Nuevo Riesgo")
    tag.click()


@then("el sistema pide:")
def step_impl(context):
    assert context.driver.find_element_by_name("descripcion") is not None
    assert context.driver.find_element_by_name("probabilidad") is not None
    assert context.driver.find_element_by_name("impacto") is not None
