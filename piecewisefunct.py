# Copyright 2013 Nicholas Esterer. All Rights Reserved.
# Contour Segments

class PieceWiseFunct:
    """Holds a length and a function and possibly a sublist of ContourSegments.
    The function is evaluated from [0,length), as a piecewise function."""
    length
