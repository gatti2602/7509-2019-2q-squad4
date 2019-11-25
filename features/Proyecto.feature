# Created by gatti2602 at 24/11/19
Feature: Gestion de Riesgos
  # Modulo de Alta y Cierre de Riesgos asociados al proyecto.
  # Permite el calculo de la exposicion del proyecto

  Scenario: FE17: Como PM Quiero cargar los riesgos del proyecto Para poder dar seguimiento y mostrar la exposicion

    Given que estoy viendo el detalle del proyecto
    When voy a la seccion de Riesgos
    Then el sistema lista todos los riesgos

    Given que deseo agregar un nuevo riesgo
    When ingreso a la seccion riesgo y voy a agregar uno nuevo
    Then el sistema pide:
        """ - Descripcion del riesgo
            - Probabilidad que suceda
            - Impacto del Riesgo: Alto, Medio, Bajo
            - Fecha de Cierre (Opcional)
            - Se ha presentado? (Opcional)"""