# jinja2-docker

## Usage

```shell
docker run --rm -v TEMPLATES_DIR:/templates -e TEMPLATE=TEMPLATE_FILE ghcr.io/netbek/jinja2-docker:main [CONTEXT]
```

## Examples

Clone the repository to view examples.

1. Render `./example.jinja2` without context:

    ```shell
    docker run --rm -v ./examples:/templates -e TEMPLATE=no_context.jinja2 ghcr.io/netbek/jinja2-docker:main
    ```

2. Render `./example.jinja2` with context:

    ```shell
    docker run --rm -v ./examples:/templates -e TEMPLATE=context.jinja2 ghcr.io/netbek/jinja2-docker:main "fruit=pineapple" "veg=broccoli"
    ```

## License

Copyright (c) 2023 Hein Bekker. Licensed under the GNU Affero General Public License, version 3.
