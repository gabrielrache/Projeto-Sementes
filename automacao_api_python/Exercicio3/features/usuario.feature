# language: en

Feature: Efetuar ordem de compra

  Scenario Outline: Efetuar uma ordem de compra na petstore
    Given que o usuário selecionou o animal com o id correspondente a "<id>" desejado na petstore
    Then o sistema valida se a ordem de pedido foi armazenada corretamente

    Examples:
      | id |
      | 1  |
      | 2  |
      | 3  |
      | 4  |


  Scenario Outline:  Efetuar uma remoção de ordem de compra na petstore
    Given que o usuário selecionou o id correspondente a "<id>" para remoção da ordem
    And incluiu nova ordem "<id_nova_ordem>" para o animal selecionado na petstore
    Then o sistema valida se a ordem foi removida com sucesso para a "<id>"
    Then o sistema valida se a ordem de pedido foi armazenada corretamente com "<id_nova_ordem>"

    Examples:
      | id | id_nova_ordem |
      | 1  | 5 |
      | 2  | 6 |
      | 3  | 7 |
      | 4  | 8 |
