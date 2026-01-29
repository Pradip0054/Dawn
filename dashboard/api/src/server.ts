import { Hono } from 'hono';
import type { Bindings } from './types/bindings';
import type { Job } from './types/job';

const app = new Hono<{ Bindings: Bindings }>()

const routes = app.get('/api/jobs', async (context) => {
  try {
    const { results } = await context.env.SCRAPPER_DB
      .prepare("SELECT * FROM jobs_list ORDER BY added_at DESC LIMIT 50;")
      .all<Job>();

    return context.json(results);
  } catch (err) {
    console.log(err);
    return context.json([], 500);
  }
})

export default app;
export type AppType = typeof routes;