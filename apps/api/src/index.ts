import { Elysia, t } from "elysia";
import { CloudflareAdapter } from "elysia/adapter/cloudflare-worker";
import { createProject, getProjects, validateProject } from "./services/project.service.js";

export default new Elysia({ adapter: CloudflareAdapter })
  .get("/", () => ({ status: "ok", service: "OpenCut API" }))
  .get("/projects", () => {
    return { projects: getProjects() };
  })
  .post(
    "/projects",
    ({ body, set }) => {
      if (!validateProject(body)) {
        set.status = 400;
        return { error: "Invalid project payload: name is required" };
      }
      const project = createProject(body);
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
