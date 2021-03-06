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
The OWTBinding module provides mapping for objects and tables.
"""

from sqlalchemy.orm import mapper, relationship
from objects import Stati_scheda_sistri, Stati_fisici_rifiuto, \
    Forme_giuridiche, Tipi_reg_cronologico, Operazioni_impianti, \
    Categorie_raee, Tipi_veicolo, Tipi_sede, Tipi_registrazioni_crono, \
    Numeri_onu, Localita_estere, Associazioni_categoria, \
    Stati_registro_cronologico, Tipi_imballaggi, Sottocategorie_star, \
    Tipi_documento, Classi_adr, Ruoli_aziendali, Stati_utente_idm, \
    Camere_commercio, Tipi_esito_trasporto, Stati_veicolo, Cod_rec_1013, \
    Stati_registrazioni_crono, Tipi_trasporto, Tipologie_raee, \
    Codici_cer_iii_livello, Tipi_stato_impresa, Caratteristiche_pericolo, \
    Sottotipi_veicolo, DescrittoreCatalogo, Azienda, Sede, Veicolo, \
    RegistroCronologico


class OWTBinding(object):
    """
    Base configuration class that is used for the binding.
    These are generally passed to the OWT request classes as arguments.
    """
    def __init__(self, storage_obj):
        """
        storage: OWTStorage
        """
        self.storage = storage_obj
        self.mapperStati_scheda_sistri = \
            mapper(Stati_scheda_sistri,
                self.storage.metadata_stati_scheda_sistri)
        self.mapperStati_fisici_rifiuto = \
            mapper(Stati_fisici_rifiuto,
                self.storage.metadata_stati_fisici_rifiuto)
        self.mapperForme_giuridiche = \
            mapper(Forme_giuridiche,
                self.storage.metadata_forme_giuridiche)
        self.mapperTipi_reg_cronologico = \
            mapper(Tipi_reg_cronologico,
                self.storage.metadata_tipi_reg_cronologico)
        self.mapperOperazioni_impianti = \
            mapper(Operazioni_impianti,
                self.storage.metadata_operazioni_impianti)
        self.mapperCategorie_raee = \
            mapper(Categorie_raee,
                self.storage.metadata_categorie_raee)
        self.mapperTipi_veicolo = \
            mapper(Tipi_veicolo,
                self.storage.metadata_tipi_veicolo)
        self.mapperTipi_sede = \
            mapper(Tipi_sede,
                self.storage.metadata_tipi_sede)
        self.mapperTipi_registrazioni_crono = \
            mapper(Tipi_registrazioni_crono,
                self.storage.metadata_tipi_registrazioni_crono)
        self.mapperNumeri_onu = \
            mapper(Numeri_onu,
                self.storage.metadata_numeri_onu)
        self.mapperLocalita_estere = \
            mapper(Localita_estere,
                self.storage.metadata_localita_estere)
        self.mapperAssociazioni_categoria = \
            mapper(Associazioni_categoria,
                self.storage.metadata_associazioni_categoria)
        self.mapperStati_registro_cronologico = \
            mapper(Stati_registro_cronologico,
                self.storage.metadata_stati_registro_cronologico)
        self.mapperTipi_imballaggi = \
            mapper(Tipi_imballaggi,
                self.storage.metadata_tipi_imballaggi)
        self.mapperSottocategorie_star = \
            mapper(Sottocategorie_star,
                self.storage.metadata_sottocategorie_star)
        self.mapperTipi_documento = \
            mapper(Tipi_documento,
                self.storage.metadata_tipi_documento)
        self.mapperClassi_adr = \
            mapper(Classi_adr,
                self.storage.metadata_classi_adr)
        self.mapperRuoli_aziendali = \
            mapper(Ruoli_aziendali,
                self.storage.metadata_ruoli_aziendali)
        self.mapperStati_utente_idm = \
            mapper(Stati_utente_idm,
                self.storage.metadata_stati_utente_idm)
        self.mapperCamere_commercio = \
            mapper(Camere_commercio,
                self.storage.metadata_camere_commercio)
        self.mapperTipi_esito_trasporto = \
            mapper(Tipi_esito_trasporto,
                self.storage.metadata_tipi_esito_trasporto)
        self.mapperStati_veicolo = \
            mapper(Stati_veicolo,
                self.storage.metadata_stati_veicolo)
        self.mapperCod_rec_1013 = \
            mapper(Cod_rec_1013,
                self.storage.metadata_cod_rec_1013)
        self.mapperStati_registrazioni_crono = \
            mapper(Stati_registrazioni_crono,
                self.storage.metadata_stati_registrazioni_crono)
        self.mapperTipi_trasporto = \
            mapper(Tipi_trasporto,
                self.storage.metadata_tipi_trasporto)
        self.mapperTipologie_raee = \
            mapper(Tipologie_raee,
                self.storage.metadata_tipologie_raee)
        self.mapperCodici_cer_iii_livello = \
            mapper(Codici_cer_iii_livello,
                self.storage.metadata_codici_cer_iii_livello)
        self.mapperTipi_stato_impresa = \
            mapper(Tipi_stato_impresa,
                self.storage.metadata_tipi_stato_impresa)
        self.mapperCaratteristiche_pericolo = \
            mapper(Caratteristiche_pericolo,
                self.storage.metadata_caratteristiche_pericolo)
        self.mapperSottotipi_veicolo = \
            mapper(Sottotipi_veicolo,
                self.storage.metadata_sottotipi_veicolo)
        self.mapperDescrittoreCatalogo = \
            mapper(DescrittoreCatalogo,
                self.storage.metadata_descrittorecatalogo)
        self.mapperAzienda = \
            mapper(Azienda,
                self.storage.metadata_azienda,
                properties={
                    'formaGiuridica': relationship(Forme_giuridiche),
                    'tipoStatoImpresa': relationship(Tipi_stato_impresa),
                    'sedeLegale': relationship(Sede, uselist=False),
                    'sediSummary': relationship(Sede,
                        secondary=self.storage.metadata_sedisummary)
                }
            )
        self.mapperSede = \
            mapper(Sede,
                self.storage.metadata_sede,
                properties={
                    'tipoSede': relationship(Tipi_sede),
                    'cameraCommercio': relationship(Camere_commercio),
                    'associazioneCategoria': relationship(
                        Associazioni_categoria),
                    'sottocategorie': relationship(Sottocategorie_star,
                        secondary=self.storage.metadata_sede_sottocategorie)
                }
            )
        self.mapperVeicolo = \
            mapper(Veicolo,
                self.storage.metadata_veicolo,
                properties={
                    'tipoVeicolo': relationship(Tipi_veicolo),
                    'sottotipoVeicolo': relationship(Sottotipi_veicolo),
                    'statoVeicolo': relationship(Stati_veicolo),
                    'sede': relationship(Sede, backref='veicoli'),
                    'codiciCerIIILivello': relationship(
                        Codici_cer_iii_livello,
                        secondary=self.storage.metadata_codiciceriiilivello)
                }
            )
        self.mapperRegistroCronologico = \
            mapper(RegistroCronologico,
                self.storage.metadata_registrocronologico,
                properties={
                    'statoRegistroCronologico': relationship(
                        Stati_registro_cronologico),
                    'tipoRegCronologico': relationship(Tipi_reg_cronologico),
                    'sottocategoria': relationship(Sottocategorie_star),
                    'idSISSede': relationship(Sede,
                        backref='registricronologici')
                }
            )
