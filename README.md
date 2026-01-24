# Dawn
A Job Scrapper that scraps job list from specific career portals and store it in a database

## Environment Variables

| Name       | Description                                                             | Required |
| ---------- | ----------------------------------------------------------------------- | -------- |
| `KEYWORDS` | Keywords which will be matched with the job titles, seperated by commas | Yes      |

## How to build

- Make sure Docker is already installed in the system
- Clone this repository

  ```bash
  git clone git@github.com:BiltuDas1/Dawn.git
  ```

- Now run the following command to download and build:

  ```bash
  docker buildx build -t <image_name>:<tag_name> .
  ```
