"""
Hilfsfunktionen für den KI-Workshop.

Hier steckt keine Magie drin – nur Plot-Code und Datensätze, damit die
Notebooks übersichtlich bleiben. Wer neugierig ist: einfach reinschauen.
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
from sklearn.datasets import make_moons

# Farben für die beiden Klassen (auch für Farbenblinde unterscheidbar)
FARBE_0 = "#1F77B4"   # blau
FARBE_1 = "#E8801C"   # orange
CMAP = plt.matplotlib.colors.LinearSegmentedColormap.from_list(
    "workshop", [FARBE_0, "#FFFFFF", FARBE_1]
)


# ---------------------------------------------------------------------------
# Datensätze
# ---------------------------------------------------------------------------

def lade_monde(n=400, rauschen=0.2, seed=42):
    """
    Zwei ineinandergreifende Halbmonde – der Klassiker für Klassifikation.
    Gibt PyTorch-Tensoren zurück: X mit Form (n, 2), y mit Form (n, 1).
    """
    X, y = make_moons(n_samples=n, noise=rauschen, random_state=seed)
    X = (X - X.mean(axis=0)) / X.std(axis=0)          # Daten normieren
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
    return X, y


def lade_spirale(n_pro_klasse=300, rauschen=0.12, seed=7):
    """
    Zwei ineinander gedrehte Spiralen (je zwei volle Umdrehungen) –
    deutlich schwieriger als die Monde.
    """
    rng = np.random.default_rng(seed)
    X, y = [], []
    for klasse in range(2):
        t = np.linspace(0.6, 4 * np.pi, n_pro_klasse)
        r = t / (4 * np.pi) * 3
        x1 = r * np.cos(t + klasse * np.pi) + rng.normal(0, rauschen, n_pro_klasse)
        x2 = r * np.sin(t + klasse * np.pi) + rng.normal(0, rauschen, n_pro_klasse)
        X.append(np.stack([x1, x2], axis=1))
        y.append(np.full(n_pro_klasse, klasse))
    X = np.concatenate(X)
    y = np.concatenate(y)
    X = (X - X.mean(axis=0)) / X.std(axis=0)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
    return X, y


def teile_auf(X, y, anteil_test=0.5, seed=1):
    """Teilt einen Datensatz in Trainings- und Testdaten."""
    g = torch.Generator().manual_seed(seed)
    idx = torch.randperm(len(X), generator=g)
    n_test = int(len(X) * anteil_test)
    test, train = idx[:n_test], idx[n_test:]
    return X[train], y[train], X[test], y[test]


# ---------------------------------------------------------------------------
# Kennzahlen
# ---------------------------------------------------------------------------

def zaehle_parameter(model):
    """Wie viele Gewichte (lernbare Zahlen) hat das Modell?"""
    return sum(p.numel() for p in model.parameters())


def genauigkeit(model, X, y):
    """Anteil richtig klassifizierter Punkte (0.0 bis 1.0)."""
    with torch.no_grad():
        vorhersage = (model(X) > 0).float()
        return (vorhersage == y).float().mean().item()


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def _scatter(ax, X, y):
    X = X.detach().numpy()
    y = y.detach().numpy().ravel()
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c=FARBE_0, s=18, edgecolors="white",
               linewidths=0.4, label="Klasse 0")
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c=FARBE_1, s=18, edgecolors="white",
               linewidths=0.4, label="Klasse 1")
    ax.set_xticks([])
    ax.set_yticks([])


def plot_daten(X, y, titel="Unsere Daten", ax=None):
    """Zeigt die Punkte, eingefärbt nach Klasse."""
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 4))
    _scatter(ax, X, y)
    ax.set_title(titel)
    ax.legend(loc="upper right", fontsize=8)
    return ax


def plot_entscheidung(model, X, y, titel=None, ax=None, aufloesung=200):
    """
    Zeichnet die Entscheidungsgrenze des Modells: Für jeden Punkt der Fläche
    wird gefragt "Was würde das Modell hier sagen?" und die Fläche eingefärbt.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 4))
    Xn = X.detach().numpy()
    rand = 0.4
    xs = np.linspace(Xn[:, 0].min() - rand, Xn[:, 0].max() + rand, aufloesung)
    ys = np.linspace(Xn[:, 1].min() - rand, Xn[:, 1].max() + rand, aufloesung)
    gx, gy = np.meshgrid(xs, ys)
    gitter = torch.tensor(np.stack([gx.ravel(), gy.ravel()], axis=1), dtype=torch.float32)
    with torch.no_grad():
        p = torch.sigmoid(model(gitter)).numpy().reshape(gx.shape)
    ax.contourf(gx, gy, p, levels=np.linspace(0, 1, 11), cmap=CMAP, alpha=0.55)
    ax.contour(gx, gy, p, levels=[0.5], colors="black", linewidths=1.2)
    _scatter(ax, X, y)
    if titel is None:
        titel = f"Genauigkeit: {genauigkeit(model, X, y):.0%}"
    ax.set_title(titel)
    return ax


def plot_verlauf(verlauf, titel="Fehler (Loss) während des Trainings", ax=None):
    """Zeigt, wie der Fehler über die Epochen sinkt (oder auch nicht)."""
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 3))
    ax.plot(verlauf, color=FARBE_0)
    ax.set_xlabel("Epoche")
    ax.set_ylabel("Loss")
    ax.set_title(titel)
    ax.grid(alpha=0.3)
    return ax
