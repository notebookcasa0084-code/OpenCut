import { Elysia } from 'elysia';
import { cors } from '@elysiajs/cors';

interface Project {
  name: string;
  fps?: number;
  resolution?: string;
}

const projects: Project[] = [];

const app = new Elysia()
  .use(cors())
  .get('/projects', () => ({ projects }))
  .post('/projects', ({ body }) => {
    const newProject = body as Project;
    projects.push(newProject);
    return { success: true, project: newProject };
  })
  .listen(3000);

console.log(
  `🦊 OpenCut API is running at ${app.server?.hostname}:${app.server?.port}`
);
