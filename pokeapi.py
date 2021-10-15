#-*- coding: utf-8 -*-

import requests
import logging

logging.basicConfig(level=10,  format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',  filename='log.log', filemode='w')

log = logging.getLogger('')

POKE_EVOLUTION = 'https://pokeapi.co/api/v2/evolution-chain/'
POKE_FORM = 'https://pokeapi.co/api/v2/pokemon-form/'
POKE_SPECIES = 'https://pokeapi.co/api/v2/pokemon-species/'


def list_evolution(url=POKE_EVOLUTION, id_pokemon=1):
    """
    Recursive function to list the evolutions of the pokemon
    if there is an error it returns an empty list
    """
    v_evo = []
    v_nom = []
    url = f'{url}{id_pokemon}/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        # access pokemon name
        v_nom.append(payload['chain']['species']['name'])
        # access the first evolution
        if payload['chain']['evolves_to']:
            # ask if it has 1 evolution
            evolves_to = payload['chain']['evolves_to'][0]
            v_evo.append(evolves_to['species']['name'])
            # access the following evolution in case you have
            if 'evolves_to' in list(evolves_to.keys()) and evolves_to['evolves_to']:
                v_evo.append(evolves_to['evolves_to'][0]['species']['name'])
    else:
        msg = f"Service error: {url} answer: {response.status_code}"
        log.error(msg)
    return v_nom, v_evo


def list_form_pokemon(url=POKE_FORM, id_pokemon=1):
    """
    if there is an error it returns an empty list
    """
    v_pokeslot = []
    v_poketype = []
    v_pokeversion = []
    url = f'{url}{id_pokemon}/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        v_pokeslot.append(payload['types'][0]['slot'])
        v_poketype.append(payload['types'][0]['type']['name'])
        v_pokeversion.append(payload['version_group']['name'])
    else:
        msg = f"Service error: {url} answer: {response.status_code}"
        log.error(msg)
    return v_pokeslot, v_poketype, v_pokeversion


def list_evolution_species(url=POKE_SPECIES, pokemon='ninetales'):
    """
    Relate the pokemon api with evolution-chain by means of the pokemon-species api
    to consult its evolutions, type of relationship from many to many,
    also consult some details of the pokemon.
    """
    v_base_happiness = []
    v_capture_rate = []
    v_color = []
    v_egg_groups = []
    v_id_pokemon = []
    id_evolution = 0

    url = f'{url}{pokemon}/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        # Locate the id_evolution of the url
        parametro = payload['evolution_chain']['url'][-7:]
        trama = parametro.find('/')
        id_evolution = parametro[trama+1:-1]
        # validate if it was extracted well
        try:
            int(id_evolution)
        except Exception as error:
            id_evolution = 9999
            msg = f"Error extracting id from url: {parametro} answer: {error}"
            log.error(msg)
        v_base_happiness.append(payload['base_happiness'])
        v_capture_rate.append(payload['capture_rate'])
        v_color.append(payload['color']['name'])
        v_egg_groups = [i['name'] for i in payload['egg_groups']]
        v_id_pokemon.append(payload['id'])
    else:
        msg = f"Service error: {url} answer: {response.status_code}"
        log.error(msg)
    return v_base_happiness, v_capture_rate, v_color, v_egg_groups, v_id_pokemon, int(id_evolution)


def evolution_prevolution(v_nom, v_evo, poke):
    """
    Assign the evolution and preevolution of the pokemon according
    to the parameters it receives.
    """
    evolution = ''
    prevolution = ''
    if poke == v_nom[0]:
        if len(v_evo) > 0:
            evolution = v_evo[0]
        else:
            evolution = ''
    elif poke == v_evo[0]:
        if len(v_evo) > 1:
            evolution = v_evo[1]
        else:
            evolution = ''
        prevolution = v_nom[0]
    else:
        if len(v_evo) > 1:
            if poke == v_evo[1]:
                prevolution = v_evo[0]
        else:
            prevolution = ''
    return evolution, prevolution


def generate_structure_api(poke='bulbasaur'):
    """
    Generate final structure
    """
    msg = f"Process: {poke}"
    log.info(msg)
    v_pokeslot = list_form_pokemon(id_pokemon=poke)[0]
    v_poketype = list_form_pokemon(id_pokemon=poke)[1]
    v_pokeversion = list_form_pokemon(id_pokemon=poke)[2]
    v_base_happiness = list_evolution_species(pokemon=poke)[0]
    v_capture_rate = list_evolution_species(pokemon=poke)[1]
    v_color = list_evolution_species(pokemon=poke)[2]
    v_egg_groups = list_evolution_species(pokemon=poke)[3]

    detail_pokemon = {
              'pokeslot': v_pokeslot,
              'poketype': v_poketype,
              'pokeversion': v_pokeversion,
              'base_happiness': v_base_happiness,
              'capture_rate': v_capture_rate,
              'color': v_color,
              'v_egg_groups': v_egg_groups
        }

    id_pokemon = list_evolution_species(pokemon=poke)[4]
    id_evolution = list_evolution_species(pokemon=poke)[5]

    v_nom = list_evolution(id_pokemon=id_evolution)[0]
    v_evo = list_evolution(id_pokemon=id_evolution)[1]

    evolution = evolution_prevolution(v_nom, v_evo, poke)[0]
    prevolution = evolution_prevolution(v_nom, v_evo, poke)[1]

    res = {
            'id': id_pokemon,
            'name': v_nom,
            'detail': detail_pokemon,
            'list_evolution': v_evo,
            'evolution': evolution,
            'prevolution': prevolution
           }

    msg = f"End Process: {res}"
    log.info(msg)

    return res
