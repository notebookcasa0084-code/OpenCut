import { Elysia, t } from "elysia";
import { CloudflareAdapter } from "elysia/adapter/cloudflare-worker";
import { validateProject } from "./services/project.service";

export default new Elysia({ adapter: CloudflareAdapter })
  .get("/", () => ({ status: "ok", service: "OpenCut API" }))
  .post(
    "/projects",
    (context: { body: { name: string; fps?: number; resolution?: string } }) => {
      const isValid = validateProject(context.body);
      return { success: isValid, project: context.body };
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
