# RetroRules Dump

Extracts all the rules from the Retro Rules SQLite3 database into a RetroPath and RP2path friendly format

## Getting Started

The current implementation includes only rules that are unique and without stereo. TODO: make the user define what are the characteristics he wants with a GUI -- geuss that would be KNIME

### Prerquisites

Must download the database from the retrorule.org website (~2.4GB) and extract it to the current path (~18GB)

## Running 

```
extractAll.py /path/to/retrorules_dump.db
```
