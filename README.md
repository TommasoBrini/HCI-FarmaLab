<p align="center">
  <img src="frontend/farmalab/src/assets/images/logo.png" alt="Logo del progetto" width="200">
</p>

# 🚀 Project Overview
Questo progetto propone un sistema basato su microservizi e completamente containerizzato tramite Docker.

L’obiettivo è fornire un’architettura modulare, facilmente manutenibile e semplice da distribuire in ambienti diversi.

- Frontend: sviluppato con Node.js + Vue.js, pensato per essere coerente con i mockup di progetto.

- Backend: server Python, responsabile della gestione delle richieste del client e della logica applicativa.

- Containerizzazione: ogni componente è isolato nel proprio container, così da facilitare sviluppo, testing e deploy.

Il progetto è stato progettato seguendo principi di semplicità, scalabilità e separazione delle responsabilità.

# 📦 Requisiti
Per eseguire il progetto è necessario avere installato:
- Docker
- Docker Compose
  
# ▶️ Avvio del progetto
- Scarica o clona la repository
- Assicurati che Docker sia in esecuzione
- Esegui il comando sottostante

```
docker-compose up
```
- Al primo avvio, Docker costruirà automaticamente le immagini e avvierà tutti i servizi definiti.
- Apri l’applicazione nel browser e di norma sarà disponibile al seguente link 
```
http://localhost:3000
```

# 🛑 Spegnere i microservizi
- Per fermare i container digitare
```
docker-compose down
```