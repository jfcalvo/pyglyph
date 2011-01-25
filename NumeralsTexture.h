
struct GlyphPosition {
    int X;
    int Y;
};

struct GlyphMetrics {
    int XBearing;
    int YBearing;
    int Width;
    int Height;
    int XAdvance;
    int YAdvance;
};

struct Glyph {
    GlyphPosition Position;
    GlyphMetrics Metrics;
};

static const Glyph NumeralGlyphs[] = {
    {{ 0, 0 }, { 0, -24, 17, 25, 18, 0 }},
    {{ 20, 0 }, { 2, -24, 11, 24, 18, 0 }},
    {{ 34, 0 }, { 0, -24, 17, 24, 18, 0 }},
    {{ 54, 0 }, { 0, -24, 17, 25, 18, 0 }},
    {{ 74, 0 }, { 0, -24, 17, 24, 18, 0 }},
    {{ 94, 0 }, { 0, -23, 17, 24, 18, 0 }},
    {{ 114, 0 }, { 1, -24, 16, 25, 18, 0 }},
    {{ 133, 0 }, { 0, -24, 17, 24, 18, 0 }},
    {{ 153, 0 }, { 0, -24, 17, 25, 18, 0 }},
    {{ 173, 0 }, { 0, -24, 17, 25, 18, 0 }},
};
