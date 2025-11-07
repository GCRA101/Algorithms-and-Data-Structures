# Translation Notes: Italian to English

## Overview
This repository has been translated from Italian to English while preserving all original Italian files in the `i18n/italian/` directory.

## What Was Translated

### 1. Directory Names
All 16 lesson directories renamed from "Lezione XX" to "Lesson XX" with English topic descriptions.

### 2. File Names
- ~70 Python files renamed
- 5 Jupyter notebooks renamed
- 1 Java file renamed
- PDF files kept with original names

### 3. Code Content
- Python comments translated (ATTRIBUTI → ATTRIBUTES, METODI → METHODS, etc.)
- Algorithm descriptions and case analysis translated
- Import statements updated to reference new English module names
- Docstrings and inline comments translated where possible

### 4. Documentation
- README.md fully translated to English
- Added note about i18n/italian/ preservation

## What Was Preserved

### Original Italian Files
All original files are preserved in `i18n/italian/` with the exact original structure:
```
i18n/italian/
├── Lezione 03 - Il Costo di un Algoritmo/
├── Lezione 04 - Il Problema della Ricerca/
├── Lezione 05 - Ricorsione/
└── ... (all original directories and files)
```

### Unchanged Content
- Jupyter notebook internal content (markdown and code cells remain in Italian)
- PDF documentation files
- Binary files
- Original author attributions

## Key Translation Mappings

### Common Terms
- Lezione → Lesson
- Esercizi → Exercises
- Ordinamento → Sorting
- Strutture Dati → Data Structures
- Alberi → Trees
- Pile e Code → Stacks and Queues
- Ricorsione → Recursion
- Dizionari → Dictionaries

### Module Names
- Piolo → Peg
- Disco → Disk
- TorreHanoi → TowerOfHanoi
- ListaPuntataDoppia → DoublyLinkedList
- AlberoBinario → BinaryTree
- AlberoBinarioDiRicerca → BinarySearchTree
- AlberoRossoNero → RedBlackTree
- Coda → Queue
- Pila → Stack

## Import Updates

26 Python files had their import statements updated to reference the new English module names. For example:
- `from Piolo import Piolo` → `from Peg import Piolo`
- `from AlberoBinario import AlberoBinario` → `from BinaryTree import AlberoBinario`

## Testing

Basic testing performed:
- ✅ Import statements load correctly
- ✅ Module instantiation works
- ⚠️ Full script execution not tested (requires matplotlib/numpy dependencies)

## Future Work

If desired, the following could be done as follow-up work:
1. Translate Jupyter notebook content (markdown cells and code comments)
2. Translate any remaining Italian inline comments in Python files
3. Translate variable names if they're in Italian (currently preserved to avoid breaking code)
4. Create multilingual documentation

## Notes

- No code logic was modified
- All algorithmic functionality preserved
- Public API names not changed (class names kept as-is when imported)
- Only comments, docstrings, and file/directory names were translated
