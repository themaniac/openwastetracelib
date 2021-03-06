#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre <paolo.melchiorre@madec.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
The I{objects} module provides objects definition.
"""


class Stati_scheda_sistri(object):
    """ """
    def __init__(self, id_stato_scheda_sistri, stato_scheda_sistri):
        self.id_stato_scheda_sistri = id_stato_scheda_sistri
        self.stato_scheda_sistri = stato_scheda_sistri


class Stati_fisici_rifiuto(object):
    """ """
    def __init__(self, id_stato_fisico_rifiuto, descr_stato_fisico_rifiuto,
                    codice_stato_fisico):
        self.id_stato_fisico_rifiuto = id_stato_fisico_rifiuto
        self.descr_stato_fisico_rifiuto = descr_stato_fisico_rifiuto
        self.codice_stato_fisico = codice_stato_fisico


class Forme_giuridiche(object):
    """ """
    def __init__(self, id_tipo_forma_giuridica,
                    descrizione_forma_giuridica=None):
        self.id_tipo_forma_giuridica = id_tipo_forma_giuridica
        self.descrizione_forma_giuridica = descrizione_forma_giuridica


class Tipi_reg_cronologico(object):
    """ """
    def __init__(self, id_tipo_reg_cronologico,
                    descrizione_tipo_reg_crono=None, macro_categoria=None):
        self.id_tipo_reg_cronologico = id_tipo_reg_cronologico
        self.descrizione_tipo_reg_crono = descrizione_tipo_reg_crono
        self.macro_categoria = macro_categoria


class Operazioni_impianti(object):
    """ """
    def __init__(self, id_operazione_impianto, id_tipo_operazione_impianto,
                    operazione_impianto, ordinamento):
        self.id_operazione_impianto = id_operazione_impianto
        self.id_tipo_operazione_impianto = id_tipo_operazione_impianto
        self.operazione_impianto = operazione_impianto
        self.ordinamento = ordinamento


class Categorie_raee(object):
    """ """
    def __init__(self, id_categoria_raee, descrizione_categoria_raee):
        self.id_categoria_raee = id_categoria_raee
        self.descrizione_categoria_raee = descrizione_categoria_raee


class Tipi_veicolo(object):
    """ """
    def __init__(self, id_tipo_veicolo, descrizione, codice_tipo_veicolo=None,
                    flag_rimorchio=None):
        self.id_tipo_veicolo = id_tipo_veicolo
        self.descrizione = descrizione
        self.codice_tipo_veicolo = codice_tipo_veicolo
        self.flag_rimorchio = flag_rimorchio


class Tipi_sede(object):
    """ """
    def __init__(self, id_tipo_sede, descrizione=None):
        self.id_tipo_sede = id_tipo_sede
        self.descrizione = descrizione


class Tipi_registrazioni_crono(object):
    """ """
    def __init__(self, id_tipo_registrazione_crono, descr_tipo_reg_crono):
        self.id_tipo_registrazione_crono = id_tipo_registrazione_crono
        self.descr_tipo_reg_crono = descr_tipo_reg_crono


class Numeri_onu(object):
    """ """
    def __init__(self, id_numero_onu, descrizione_numero_onu):
        self.id_numero_onu = id_numero_onu
        self.descrizione_numero_onu = descrizione_numero_onu


class Localita_estere(object):
    """ """
    def __init__(self, id_localita, nazione, sigla_nazione):
        self.id_localita = id_localita
        self.nazione = nazione
        self.sigla_nazione = sigla_nazione


class Associazioni_categoria(object):
    """ """
    def __init__(self, id_associazione_categoria, ass_categoria_nome=None,
                    id_accordo=None, sigla_provincia=None, sigla_cciaa=None):
        self.id_associazione_categoria = id_associazione_categoria
        self.ass_categoria_nome = ass_categoria_nome
        self.id_accordo = id_accordo
        self.sigla_provincia = sigla_provincia
        self.sigla_cciaa = sigla_cciaa


class Stati_registro_cronologico(object):
    """ """
    def __init__(self, id_stato_registro_cronologico,
                    descrizione_stato_reg_crono):
        self.id_stato_registro_cronologico = id_stato_registro_cronologico
        self.descrizione_stato_reg_crono = descrizione_stato_reg_crono


class Tipi_imballaggi(object):
    """ """
    def __init__(self, id_tipo_imballaggio, tipo_imballaggio,
                    codice_imballaggio):
        self.id_tipo_imballaggio = id_tipo_imballaggio
        self.tipo_imballaggio = tipo_imballaggio
        self.codice_imballaggio = codice_imballaggio


class Sottocategorie_star(object):
    """ """
    def __init__(self, id_sottocategoria_star, id_categoria_star=None,
                    descrizione_sottocategoria=None):
        self.id_sottocategoria_star = id_sottocategoria_star
        self.id_categoria_star = id_categoria_star
        self.descrizione_sottocategoria = descrizione_sottocategoria


class Tipi_documento(object):
    """ """
    def __init__(self, id_tipo_documento, descrizione):
        self.id_tipo_documento = id_tipo_documento
        self.descrizione = descrizione


class Classi_adr(object):
    """ """
    def __init__(self, id_classe_adr, descrizione_classe_adr):
        self.id_classe_adr = id_classe_adr
        self.descrizione_classe_adr = descrizione_classe_adr


class Ruoli_aziendali(object):
    """ """
    def __init__(self, id_ruolo_aziendale, ruolo_aziendale):
        self.id_ruolo_aziendale = id_ruolo_aziendale
        self.ruolo_aziendale = ruolo_aziendale


class Stati_utente_idm(object):
    """ """
    def __init__(self, id_stato_utente_idm):
        self.id_stato_utente_idm = id_stato_utente_idm


class Camere_commercio(object):
    """ """
    def __init__(self, id_camera_commercio, indirizzo=None, numero_civico=None,
                    cap=None, nome_persona_riferimento=None,
                    cognome_persona_riferimento=None,
                    email_persona_riferimento=None,
                    telefono_persona_riferimento=None, sigla_cciaa=None):
        self.id_camera_commercio = id_camera_commercio
        self.indirizzo = indirizzo
        self.numero_civico = numero_civico
        self.cap = cap
        self.nome_persona_riferimento = nome_persona_riferimento
        self.cognome_persona_riferimento = cognome_persona_riferimento
        self.email_persona_riferimento = email_persona_riferimento
        self.telefono_persona_riferimento = telefono_persona_riferimento
        self.sigla_cciaa = sigla_cciaa


class Tipi_esito_trasporto(object):
    """ """
    def __init__(self, id_esito_trasporto, descr_esito_trasporto):
        self.id_esito_trasporto = id_esito_trasporto
        self.descr_esito_trasporto = descr_esito_trasporto


class Stati_veicolo(object):
    """ """
    def __init__(self, id_stato_veicolo, descrizione_stato_veicolo):
        self.id_stato_veicolo = id_stato_veicolo
        self.descrizione_stato_veicolo = descrizione_stato_veicolo


class Cod_rec_1013(object):
    """ """
    def __init__(self, id_cod_rec_1013, descrizione_cod_rec):
        self.id_cod_rec_1013 = id_cod_rec_1013
        self.descrizione_cod_rec = descrizione_cod_rec


class Stati_registrazioni_crono(object):
    """ """
    def __init__(self, id_stato_registrazione_crono,
                    descrizione_stato_reg_crono):
        self.id_stato_registrazione_crono = id_stato_registrazione_crono
        self.descrizione_stato_reg_crono = descrizione_stato_reg_crono


class Tipi_trasporto(object):
    """ """
    def __init__(self, id_tipo_trasporto, descrizione_tipo_trasporto):
        self.id_tipo_trasporto = id_tipo_trasporto
        self.descrizione_tipo_trasporto = descrizione_tipo_trasporto


class Tipologie_raee(object):
    """ """
    def __init__(self, id_tipologia_raee, descrizione_tipologia_raee):
        self.id_tipologia_raee = id_tipologia_raee
        self.descrizione_tipologia_raee = descrizione_tipologia_raee


class Codici_cer_iii_livello(object):
    """ """
    def __init__(self, id_codice_cer_iii_livello, escrizione_iii_livello,
                    flag_pericoloso, flag_attivo):
        self.id_codice_cer_iii_livello = id_codice_cer_iii_livello
        self.escrizione_iii_livello = escrizione_iii_livello
        self.flag_pericoloso = flag_pericoloso
        self.flag_attivo = flag_attivo


class Tipi_stato_impresa(object):
    """ """
    def __init__(self, id_tipo_stato_impresa):
        self.id_tipo_stato_impresa = id_tipo_stato_impresa


class Caratteristiche_pericolo(object):
    """ """
    def __init__(self, id_caratteristica_pericolo, descr_car_pericolo):
        self.id_caratteristica_pericolo = id_caratteristica_pericolo
        self.descr_car_pericolo = descr_car_pericolo


class Sottotipi_veicolo(object):
    """ """
    def __init__(self, id_sottotipo_veicolo, descrizione,
                    codice_sottotipo_veicolo=None):
        self.id_sottotipo_veicolo = id_sottotipo_veicolo
        self.descrizione = descrizione
        self.codice_sottotipo_veicolo = codice_sottotipo_veicolo


class DescrittoreCatalogo(object):
    """ """
    def __init__(self, catalogo, versione, descrizione):
        self.catalogo = catalogo
        self.versione = versione
        self.descrizione = descrizione


class Azienda(object):
    """ Azienda object with idSIS."""
    def __init__(self, ragioneSociale, codiceFiscale, versione, idSIS,
                    **kwargs):
        self.ragioneSociale = ragioneSociale
        self.codiceFiscale = codiceFiscale
        self.versione = versione
        self.idSIS = idSIS
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Sede(object):
    """ Sede object with idSIS. """
    def __init__(self, nomeSede, codiceIstatLocalita, codiceCatastale, nazione,
                    siglaNazione, indirizzo, versione, idSIS, tipoSede=None,
                    **kwargs):
        self.nomeSede = nomeSede
        self.codiceIstatLocalita = codiceIstatLocalita
        self.codiceCatastale = codiceCatastale
        self.nazione = nazione
        self.siglaNazione = siglaNazione
        self.indirizzo = indirizzo
        self.versione = versione
        self.tipoSede = tipoSede
        self.idSIS = idSIS
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Veicolo(object):
    """ Veicolo object with idSIS. """
    def __init__(self, targa, tipoVeicolo=None, statoVeicolo=None,
                    **kwargs):
        self.targa = targa
        self.tipoVeicolo = tipoVeicolo
        self.statoVeicolo = statoVeicolo
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class RegistroCronologico(object):
    """ RegistroCronologico object with idSIS. """
    def __init__(self, idSIS, codiceRegistroCronologico, versione,
                    ultimoNumero, dataUltimoNumero, sottocategoria=None,
                    statoRegistroCronologico=None, tipoRegCronologico=None,
                    **kwargs):
        self.idSIS = idSIS
        self.codiceRegistroCronologico = codiceRegistroCronologico
        self.versione = versione
        self.ultimoNumero = ultimoNumero
        self.dataUltimoNumero = dataUltimoNumero
        self.statoRegistroCronologico = statoRegistroCronologico
        self.tipoRegCronologico = tipoRegCronologico
        self.sottocategoria = sottocategoria
        for key in kwargs:
            self.__setattr__(key, kwargs[key])
