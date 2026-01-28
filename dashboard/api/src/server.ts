import { Hono } from 'hono';

const app = new Hono<{ Bindings: Bindings }>()

app.get('/api/jobs', async (context) => {
  try {
    const { results } = await context.env.SCRAPPER_DB
      .prepare("SELECT * FROM jobs_list ORDER BY added_at DESC LIMIT 50;")
      .all();

    return context.json(results);
  } catch (err) {
    console.log(err);
    return context.json({ message: "Database error" }, 500);
  }
})

export default app;
