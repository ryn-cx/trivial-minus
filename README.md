# Trivial Minus

[Paramount+](https://www.paramountplus.com) API wrapper built using [Good Ass
Pydantic Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and
[Get Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/trivial-minus
```

## Usage

Every endpoint is called to get the parsed model, and `download()` and `load()`
are the two halves of that.

```python
from trivial_minus import TrivialMinus

client = TrivialMinus()

show = client.show("south-park")
print(show.seasons)  # [1, 2, 3, ...]

episodes = client.episodes("south-park", season_number=28)
for episode in episodes.result.data:
    print(episode.episode_number, episode.title)

movie = client.movie("ALVE01KT235XQDEK58R7H2012VNZMK")
print(movie.name, movie.content_rating)

# A section is one of the video carousels on a show page, such as Clips.
for listed_section in show.sections:
    section = client.section("south-park", section_id=listed_section.id)
    print(section.title, section.total)
    for video in section.data:
        print(video.title, video.content_id)
```
