import json
import locale
import pandas as pd
import pyqtgraph as pg
import numpy as np
 
locale.setlocale(locale.LC_ALL, "C")
 
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

 
REQUIRED_COLS = {"date", "city", "temp_c", "humidity", "rainfall_mm", "condition"}
CONDITIONS    = ["Sunny", "Cloudy", "Rainy", "Stormy"]
CITIES        = ["Bangkok", "Chiang Mai", "Phuket"]
 
 
 
def read_csv(path: str) -> pd.DataFrame:
    """
    TODO 1 — Read a CSV file and return a clean DataFrame.
    - Read csv file into a pandas DataFrame
    - Raise ValueError if the file is empty
    - Raise ValueError if any required columns are missing
    - Return the DataFrame
    """
    df = pd.read_csv(path)
 
    if df.empty:
        raise ValueError(f"The CSV file '{path}' is empty.")
 
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")
 
    return df
 
 
def read_json(path: str) -> pd.DataFrame:
    """
    TODO 2 — Read a JSON file and return a DataFrame.
    - Read json file into a pandas DataFrame
    - Raise ValueError if the file is empty
    - Raise ValueError if any required columns are missing
    - Return the DataFrame
    """
    df = pd.read_json(path)
 
    if df.empty:
        raise ValueError(f"The JSON file '{path}' is empty.")
 
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"JSON is missing required columns: {sorted(missing)}")
 
    return df
 
 
def write_csv(df: pd.DataFrame, path: str) -> None:
    """
    TODO 3 — Save a DataFrame to a CSV file.
    - Raise ValueError if the DataFrame is empty
    - Raise IOError if writing fails
    """
    if df.empty:
        raise ValueError("Cannot save an empty DataFrame to CSV.")
 
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        raise IOError(f"Failed to write CSV to '{path}': {e}")
 
 
def write_json(df: pd.DataFrame, path: str) -> None:
    """
    TODO 4 — Save a DataFrame to a JSON file.
    - Raise ValueError if the DataFrame is empty
    - Raise IOError if writing fails
    """
    if df.empty:
        raise ValueError("Cannot save an empty DataFrame to JSON.")
 
    try:
        df.to_json(path, orient="records", indent=2)
    except Exception as e:
        raise IOError(f"Failed to write JSON to '{path}': {e}")
 
 
def _to_arabic(text: str) -> str:
    """Convert any Eastern-Arabic / Thai digits in a string to ASCII digits."""
    result = []
    for ch in text:
        cp = ord(ch)

        if 0x0E50 <= cp <= 0x0E59:
            result.append(chr(cp - 0x0E50 + ord('0')))

        elif 0x0660 <= cp <= 0x0669:
            result.append(chr(cp - 0x0660 + ord('0')))

        elif 0x06F0 <= cp <= 0x06F9:
            result.append(chr(cp - 0x06F0 + ord('0')))
        else:
            result.append(ch)
    return "".join(result)
 
 
def build_stats(df: pd.DataFrame) -> QTableWidget:
    """
    TODO 5 — Return a QTableWidget with per-city summary statistics.
    Layout: rows = metrics, columns = cities  (matches example in spec)
    """
    if df.empty:
        raise ValueError("Cannot build statistics from an empty DataFrame.")
 
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"DataFrame is missing required columns: {sorted(missing)}")

    city_stats = {}
    for city in CITIES:
        city_df = df[df["city"] == city]
        if city_df.empty:
            city_stats[city] = ["0", "—", "—", "—", "—", "—"]
        else:
            n          = len(city_df)
            avg_temp   = float(city_df["temp_c"].mean())
            max_temp   = float(city_df["temp_c"].max())
            min_temp   = float(city_df["temp_c"].min())
            total_rain = float(city_df["rainfall_mm"].sum())
            avg_hum    = float(city_df["humidity"].mean())
            city_stats[city] = [
                "{:d}".format(n),
                "{:.1f}".format(avg_temp),
                "{:.1f}".format(max_temp),
                "{:.1f}".format(min_temp),
                "{:.1f}".format(total_rain),
                "{:.1f}".format(avg_hum),
            ]

    row_labels = ["records", "avg_temp", "max_temp", "min_temp",
                  "total_rain", "avg_humidity"]
 
    n_rows = len(row_labels)
    n_cols = len(CITIES) + 1
 
    table = QTableWidget(n_rows, n_cols)
    table.setHorizontalHeaderLabels(["city"] + CITIES)
    table.verticalHeader().setVisible(False)
    table.setEditTriggers(QTableWidget.NoEditTriggers)
    table.setAlternatingRowColors(True)

    table.horizontalHeader().setStretchLastSection(False)
    table.horizontalHeader().setSectionResizeMode(
        __import__("PySide6.QtWidgets", fromlist=["QHeaderView"]).QHeaderView.ResizeToContents
    )
 
    city_colors = {
        "Bangkok":    QColor(255, 220, 120, 140),
        "Chiang Mai": QColor(120, 195, 255, 140),
        "Phuket":     QColor(120, 220, 160, 140),
    }
 
    bold = QFont()
    bold.setBold(True)
 
    for row_idx, label in enumerate(row_labels):
        lbl_item = QTableWidgetItem(label)
        lbl_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        lbl_item.setFont(bold)
        table.setItem(row_idx, 0, lbl_item)

        for col_idx, city in enumerate(CITIES, start=1):
            raw   = city_stats[city][row_idx]
            value = _to_arabic(raw)
            item  = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignCenter)
            item.setBackground(city_colors.get(city, QColor(230, 230, 230, 100)))
            table.setItem(row_idx, col_idx, item)
 
    return table
 
 
def show_chart(df: pd.DataFrame, chart_type: str) -> pg.PlotWidget:
    """
    TODO 6 — Draw a Rainfall Histogram using pyqtgraph and return a PlotWidget.
    - Raise ValueError if the DataFrame has no data
    - Raise ValueError if rainfall_mm column is missing
    - Return a pg.PlotWidget with the histogram rendered
    """
    if df is None or df.empty:
        raise ValueError("Cannot draw chart: DataFrame is empty.")
 
    if "rainfall_mm" not in df.columns:
        raise ValueError("Cannot draw chart: 'rainfall_mm' column is missing.")
 
    rainfall = df["rainfall_mm"].dropna().values

    rainy = rainfall[rainfall > 0]
    if len(rainy) == 0:
        rainy = rainfall
 
    counts, bin_edges = np.histogram(rainy, bins=10)

    plot = pg.PlotWidget()
    plot.setBackground("w")
    plot.setTitle("Rainfall Distribution (rainy days)", color="#333333", size="12pt")
    plot.setLabel("left",   "Number of Days")
    plot.setLabel("bottom", "Rainfall (mm)")
    plot.showGrid(x=True, y=True, alpha=0.3)
 
    bar_width = bin_edges[1] - bin_edges[0]
    bar_x     = bin_edges[:-1]
 
    bars = pg.BarGraphItem(
        x=bar_x,
        height=counts,
        width=bar_width * 0.85,
        brush=pg.mkBrush(100, 180, 255, 200),
        pen=pg.mkPen("w", width=1),
    )
    plot.addItem(bars)

    for x, h in zip(bar_x, counts):
        if h > 0:
            label = pg.TextItem(str(int(h)), anchor=(0.5, 1.0), color="#333333")
            label.setPos(x + bar_width / 2, h)
            plot.addItem(label)
 
    return plot