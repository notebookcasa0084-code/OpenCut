import { Elysia, t } from "elysia";
import { CloudflareAdapter } from "elysia/adapter/cloudflare-worker";
import { createProject, getProjects, validateProject } from "./services/project.service";

export default new Elysia({ adapter: CloudflareAdapter })
  .get("/", () => ({ status: "ok", service: "OpenCut API" }))
  .get("/projects", () => ({ projects: getProjects() }))
  .post(
    "/projects",
    (context: { body: { name: string; fps?: number; resolution?: string } }) => {
      if (!validateProject(context.body)) {
        return { success: false, error: "Invalid project name" };
      }
      const project = createProject(context.body);
      return { success: true, project };
    },
    {
      body: t.Object({
        name: t.String(),
        fps: t.Optional(t.Number()),
        resolution: t.Optional(t.String()),
      }),
    }
  )
  .compile();
