import { useState } from 'react';
import { hc } from 'hono/client';
import type { AppType } from '../../../api/src/server';
import type { Job } from '../../../api/src/types/job';


export function useJobsList() {
  const client = hc<AppType>('/');
  const [result, setResult] = useState<Job[] | null>(null);
  const [error, setError] = useState<any | null>(null);

  async function fetchJobs() {
    try {
      const response = await client.api.jobs.$get();
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setError(error);
    }
  }

  return { fetchJobs, result, error };
}