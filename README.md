# jinja2-docker

## Usage

```shell
docker run --rm -v TEMPLATES_DIR:/templates -e TEMPLATE=TEMPLATE_FILE ghcr.io/netbek/jinja2-docker:latest [CONTEXT]
```

## Examples

Clone the repository to view examples.

1. Render a template without context:

    ```shell
    docker run --rm -v ./examples:/templates -e TEMPLATE=no_context.jinja2 ghcr.io/netbek/jinja2-docker:latest
    ```

2. Render a template with context:

    ```shell
    docker run --rm -v ./examples:/templates -e TEMPLATE=context.jinja2 ghcr.io/netbek/jinja2-docker:latest "fruit=pineapple" "veg=broccoli"
    ```

3. Render a template and format with Prettier:

    ```shell
    docker run --rm -v ./examples:/templates -e TEMPLATE=file.yml.jinja2 -e PRETTY=1 -e PRETTIER_PARSER=yaml ghcr.io/netbek/jinja2-docker:latest "fruit=pineapple" "veg=broccoli"
    ```

## License

Copyright (c) 2023 Hein Bekker. Licensed under the GNU Affero General Public License, version 3.
