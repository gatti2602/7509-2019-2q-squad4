# Created by gatti2602 at 10/11/19
Feature: Gestion de Features (FE118)

  Scenario: Alta de Features
    Given que hay features en el sistema
    When indico al sistema que muestre los features
    Then obtengo una lista de todos los features en desarrollo

  Scenario: Alta de Features desde Form Web
    Given que ingreso a la pagina de carga de features
    When completo los valores description, expected_date y status
    Then el feature se crea en el sistema

