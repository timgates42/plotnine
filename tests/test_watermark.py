from pathlib import Path

import pandas as pd
from plotnine import ggplot, aes, geom_point, watermark


wm_file = Path(__file__).parent / 'images/plotnine-watermark.png'


def test_watermark():
    df = pd.DataFrame({
        'x': [1, 2, 3],
        'y': [1, 2, 3]
    })

    p = (ggplot(df)
         + geom_point(aes('x', 'y'))
         + watermark(wm_file, 150, 160)
         + watermark(wm_file, 150, 210, 0.5)
         )

    assert p == 'watermark'
