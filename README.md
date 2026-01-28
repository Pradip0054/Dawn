# Dawn
A Job Scrapper that scraps job list from specific career portals and store it in a database

## Environment Variables

| Name                      | Description                                                             | Required |
| ------------------------- | ----------------------------------------------------------------------- | -------- |
| `KEYWORDS`                | Keywords which will be matched with the job titles, seperated by commas | Yes      |
| `CLOUDFLARE_API_KEY`      | Cloudflare Workers API Key                                              | Yes*     |
| `CLOUDFLARE_ACCOUNT_ID`   | Cloudflare Workers Account ID                                           | Yes*     |
| `CLOUDFLARE_DATABASE_ID`  | Cloudflare D1 Database ID                                               | Yes*     |
| `CLOUDFLARE_KV_NAMESPACE` | Cloudflare KV Database Namespace ID                                     | Yes*     |

> *These are required only on Production environment, not in development environment

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
