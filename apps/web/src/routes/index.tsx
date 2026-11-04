import { createFileRoute } from "@tanstack/react-router";
import { CreateProjectForm } from "../components/CreateProjectForm";
import { Timeline } from "../components/Timeline";

export const Route = createFileRoute("/")({
  component: HomeComponent,
});

function HomeComponent() {
  const sampleClips = [
    { id: "1", name: "Intro Video", duration: 5, type: "video" as const },
    { id: "2", name: "Background Track", duration: 15, type: "audio" as const },
    { id: "3", name: "Main Title", duration: 3, type: "text" as const },
  ];

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif", display: "flex", flexDirection: "column", gap: "2rem" }}>
      <div>
        <h1>OpenCut Video Editor</h1>
        <p>Monorepo modernizado com TanStack Router, Elysia e moon.</p>
      </div>

      <hr style={{ border: "none", borderTop: "1px solid #eaeaea" }} />

      <Timeline clips={sampleClips} />

      <hr style={{ border: "none", borderTop: "1px solid #eaeaea" }} />

      <CreateProjectForm />
    </main>
  );
}
