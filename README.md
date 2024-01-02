# jinja2-docker

## Usage

```shell
docker run --rm -v TEMPLATES_DIR:/templates -e TEMPLATE=TEMPLATE_FILE jinja2-docker [CONTEXT]
```

## Examples

Render `./example.jinja2` without context:

```shell
docker run --rm -v .:/templates -e TEMPLATE=example.jinja2 jinja2-docker
```

Render `./example.jinja2` with context:

```shell
docker run --rm -v .:/templates -e TEMPLATE=example.jinja2 jinja2-docker "key=value" "other_key=other_value"
```

## License

Copyright (c) 2023 Hein Bekker. Licensed under the GNU Affero General Public License, version 3.
