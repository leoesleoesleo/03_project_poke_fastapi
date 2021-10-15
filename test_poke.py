# -*- coding: utf-8 -*-

import requests
import pytest
from pokeapi import *
from mocks import *

@pytest.mark.parametrize("url,expected", 
                         [(POKE_EVOLUTION, 200),
                          (POKE_FORM, 200),
                          (POKE_SPECIES, 200)])
def test_api_response(url, expected):
    """
    Test that the apis respond pokeapi
    """
    url = f'{url}1/'
    response = requests.get(url)
    assert response.status_code == expected


@pytest.mark.parametrize("id_pokemon,expected", 
                         [(33, (['slowpoke'], ['slowbro'])),
                         (45, (['exeggcute'], ['exeggutor'])),
                         (96, (['wooper'], ['quagsire'])),
                         (105, (['snubbull'], ['granbull'])),
                         (150, (['mawile'], []))])
def test_list_evolution(id_pokemon, expected):
    """
    Test that the function responds correctly
    """
    assert list_evolution(id_pokemon=id_pokemon) == expected


@pytest.mark.parametrize("id_pokemon,expected", 
                         [(38, ([1], ['fire'], ['red-blue'])),
                         (109, ([1], ['poison'], ['red-blue'])),
                         (155, ([1], ['fire'], ['gold-silver'])),
                         (196, ([1], ['psychic'], ['gold-silver']))])
def test_list_form_pokemon(id_pokemon, expected):
    """
    Test that the function responds correctly
    """
    assert list_form_pokemon(id_pokemon=id_pokemon) == expected


@pytest.mark.parametrize("pokemon,expected", 
                         [('liepard', ([70], [90], ['purple'], ['ground'], [510], 261)),
                         ('cursola', ([50], [30], ['white'], [], [864], 113)),
                         ('snom', ([50], [190], ['white'], [], [872], 454)),
                         ('cufant', ([50], [190], ['yellow'], [], [878], 459)),
                         ('kubfu', ([50], [3], ['gray'], [], [891], 469))])
def test_list_evolution_species(pokemon, expected):
    """
    Test that the function responds correctly
    """
    assert list_evolution_species(pokemon=pokemon) == expected


@pytest.mark.parametrize("v_nom,v_evo,poke,expected", 
                         [(['krabby'], ['kingler'], 'krabby', ('kingler', '') ),
                         (['koffing'], ['weezing'], 'weezing', ('', 'koffing') ),
                         (['rhyhorn'],['rhydon', 'rhyperior'],'rhydon', ('rhyperior', 'rhyhorn')),
                         (['hoothoot'],['noctowl'],'noctowl', ('', 'hoothoot')),
                         (['suicune'],[],'suicune', ('', '') )])
def test_evolution_prevolution(v_nom,v_evo,poke,expected):
    """
    Test that the function responds correctly
    """
    assert evolution_prevolution(v_nom=v_nom, v_evo=v_evo, poke=poke) == expected


@pytest.mark.parametrize("poke,expected",
                         [('ninetales', data_test_ninetales),
                         ('golduck', data_test_golduck),
                         ('machoke', data_test_machoke),
                         ('magnemite', data_test_magnemite ),
                         ('lapras', data_test_lapras )])
def test_generate_structure_api(poke,expected):
    """
    Test that the function responds correctly
    """
    assert generate_structure_api(poke=poke) == expected
