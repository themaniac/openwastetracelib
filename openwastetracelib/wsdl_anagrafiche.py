# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre
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
The I{wsdl cataloghi} module provides connection to GetElencoCataloghi method.
"""

import __builtin__

from xml.etree import cElementTree as ElementTree

from https_cert import HttpAuthUsingCert
from suds.client import Client

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session

import config
from db_objects import *
from db_metadata import *
from db_mapper import *


#import cataloghi
#from cataloghi import *

## TODO: echo =True e da elimnare in un ambiente di produzione
dbengine = create_engine(config.DB_STRING, echo=False)
meta = MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session = Session()

# Connessione al Web services
transport = HttpAuthUsingCert(config.CER_PATH, config.PEM_PATH)
client = Client(config.WSDL_URL, transport=transport)

def GetAzienda (codiceFiscaleAzienda):

    # Recupero dell'elenco cataloghi
    aziendaS = client.service.GetAzienda(config.USER_ID,"",codiceFiscaleAzienda)

    a1=Azienda(ragioneSociale= str(aziendaS.ragioneSociale),
               cognome=aziendaS.cognome.__repr__(),
               nome=aziendaS.nome.__repr__(),
               formaGiuridica=aziendaS.formaGiuridica.idCatalogo.__repr__(),
               formaGiuridicaDescr=aziendaS.formaGiuridica.description.__repr__(),
               tipoStatoImpresa=aziendaS.tipoStatoImpresa.idCatalogo.__repr__(),
               tipoStatoImpresaDescr=aziendaS.tipoStatoImpresa.description.__repr__(),
               codiceFiscale=aziendaS.codiceFiscale.__repr__(),
               pIva=aziendaS.pIva.__repr__(),
               numeroIscrizioneAlbo=aziendaS.numeroIscrizioneAlbo.__repr__(),
               cciaaRea=aziendaS.cciaaRea.__repr__(),
               numeroIscrizioneRea=aziendaS.numeroIscrizioneRea.__repr__(),
               codiceIstatAttPrincipale=aziendaS.codiceIstatAttPrincipale.__repr__(),
               dataIscrizioneStar=aziendaS.dataIscrizioneStar,   # nei campi datetime se c'e' la stringa none si incazza allora non faccio il repr
               codiceAtecoAttPrincipale=aziendaS.codiceAtecoAttPrincipale.__repr__(),
               descrizioneAttPrincipale=aziendaS.descrizioneAttPrincipale.__repr__(),
               versione=2,   #fixme: aziendaS.versione.__repr__(), mi restituisce '2L' e non va bene
               idSIS=aziendaS.idSIS.__repr__()
               )
    session.add(a1)


#tipoSede,tipoSedeDescr,nomeSede,codiceIstatLocalita,codiceCatastale,nazione,siglaNazione,indirizzo,nrCivico,cap,versione,idSIS
    SL=SedeLegale(tipoSede= aziendaS.sedeLegale.tipoSede.idCatalogo.__repr__(),
               tipoSedeDescr=aziendaS.sedeLegale.tipoSede.description.__repr__(),
               nomeSede=aziendaS.sedeLegale.nomeSede.__repr__(),
               codiceIstatLocalita=aziendaS.sedeLegale.codiceIstatLocalita.__repr__(),
               codiceCatastale=aziendaS.sedeLegale.codiceCatastale.__repr__(),
               nazione=aziendaS.sedeLegale.nazione.__repr__(),
               siglaNazione=aziendaS.sedeLegale.siglaNazione.__repr__(),
               indirizzo=aziendaS.sedeLegale.indirizzo.__repr__(),
               nrCivico=aziendaS.sedeLegale.nrCivico.__repr__(),
               cap=aziendaS.sedeLegale.cap.__repr__(),
               versione=2,   #fixme: aziendaS.versione.__repr__(), mi restituisce '2L' e non va bene
               idSIS=aziendaS.sedeLegale.idSIS.__repr__()   #fixme
               )
    a1.RelSedeLegale.append(SL)
    session.add(SL)



    for s in aziendaS.sediSummary:
        Sede1=Sede(
            tipoSede = str(s.tipoSede.idCatalogo),
            tipoSedeDescr = str(s.tipoSede.description),
            nomeSede = str(s.nomeSede),
            codiceIstatLocalita = str(s.codiceIstatLocalita),
            codiceCatastale = str(s.codiceCatastale),
            nazione = str(s.nazione),
            siglaNazione = str(s.siglaNazione),
            indirizzo = str(s.indirizzo),
            nrCivico = str(s.nrCivico),
            cap = str(s.cap),
            #fixme: non dovrebbero essere commentati
            #telefono = str(s.telefono),
            #fax = str(s.fax),
            #numeroAddetti = int(s.numeroAddetti),
            #cameraCommercio = str(s.cameraCommercio),
            #cameraCommercioDescr = str(s.cameraCommercioDescr),
            #associazioneCategoria = str(s.associazioneCategoria),
            #associazioneCategoriaDescr = str(s.associazioneCategoriaDescr),
            #codiceIstatAttPrincipale = str(s.codiceIstatAttPrincipale),
            #codiceAtecoAttPrincipale = str(s.codiceAtecoAttPrincipale),
            #descrizioneAttPrincipale = str(s.descrizioneAttPrincipale),
            #numeroIscrizioneRea = str(s.numeroIscrizioneRea),
            #numeroUla = str(s.numeroUla),
            #latitudine = str(s.latitudine),
            #longitudine = str(s.longitudine),
            #fixme: qui sotto non dovrebbe essere 1 ma s.versione
            versione = 1,
            idSIS = str(s.idSIS)
            )
        a1.RelSedi.append(Sede1)
        session.add(Sede1)


    session.commit()



GetAzienda ('00090710690')
