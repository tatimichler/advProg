# Einrichten

`git init`

Initialisiert ein neues Git-Repository im aktuellen Verzeichnis.

`git config --global user.name "[Name]"`

Setzt den Benutzernamen für Git, der bei Commits als Autor angezeigt wird. [Name] sollte durch deinen Namen ersetzt werden.

`git config --global user.email "[E-Mail-Adresse]"`

Setzt die E-Mail-Adresse für Git, die bei Commits als Autor angezeigt wird. [E-Mail-Adresse] sollte durch deine E-Mail-Adresse ersetzt werden.

# Arbeiten mit Änderungen

`git status`

Zeigt den Status des Arbeitsverzeichnisses an, einschließlich aller Dateien, die verändert oder hinzugefügt wurden.

`git add [Dateiname]`

Fügt eine bestimmte Datei dem Index hinzu, um sie für den nächsten Commit zu markieren.

`git add .`

Fügt alle Änderungen im aktuellen Verzeichnis dem Index hinzu, um sie für den nächsten Commit zu markieren.

`git commit -m "[Nachricht]"`

Erstellt einen neuen Commit mit den Änderungen im Index und einer Commit-Nachricht.

`git commit -a`

Fügt alle Änderungen im Arbeitsverzeichnis dem Index hinzu und erstellt einen neuen Commit mit einer Commit-Nachricht.

`git diff`

Zeigt die Unterschiede zwischen dem Arbeitsverzeichnis und dem Index an.

`git diff --staged`

Zeigt die Unterschiede zwischen dem Index und dem letzten Commit an.

# Verwalten von Commits

`git log`

Zeigt eine Liste aller Commits im Repository an.

`git log --oneline`

Zeigt eine kurze Liste aller Commits im Repository an, jede Zeile entspricht einem Commit.

`git checkout [Commit-Hash]`

Wechselt zum Commit mit dem angegebenen Hash-Wert.

`git revert [Commit-Hash]`

Erstellt einen neuen Commit, der die Änderungen des angegebenen Commits rückgängig macht.

`git reset [Commit-Hash]`

Löscht alle Commits nach dem angegebenen Commit und setzt den Index und das Arbeitsverzeichnis auf den Stand des angegebenen Commits zurück.

`git reset --hard [Commit-Hash]`

Löscht alle Commits nach dem angegebenen Commit und setzt den Index und das Arbeitsverzeichnis auf den Stand des angegebenen Commits zurück, ohne die Änderungen zu behalten. ACHTUNG: Alle ungespeicherten Änderungen im Arbeitsverzeichnis gehen verloren!

# Arbeiten mit Branches

`git branch`

Zeigt eine Liste aller Branches im Repository an.

`git branch [Branch-Name]`

Erstellt einen neuen Branch mit dem angegebenen Namen.

`git checkout [Branch-Name]`

Wechselt zum Branch mit dem angegebenen Namen.

`git merge [Branch-Name]`

Führt die Änderungen des angegebenen Branches in den aktuellen Branch zusammen.

`git branch -d [Branch-Name]`

Löscht den Branch mit dem angegebenen Namen, nachdem alle Änderungen in einem anderen Branch zusammengeführt wurden.

# Remote-Repository

`git remote add origin [Repository-URL]`

Fügt ein Remote-Repository hinzu, das mit dem Namen "origin" verknüpft ist und das angegebene Repository-URL verwendet
