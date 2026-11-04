export interface ProjectPayload {
  id?: string;
  name: string;
  fps?: number;
  resolution?: string;
  createdAt?: string;
}

const projects: ProjectPayload[] = [];

export function getProjects(): ProjectPayload[] {
  return projects;
}

export function createProject(payload: ProjectPayload): ProjectPayload {
  const newProject: ProjectPayload = {
    id: Math.random().toString(36).substring(2, 9),
    name: payload.name.trim(),
    fps: payload.fps || 60,
    resolution: payload.resolution || "1080p",
    createdAt: new Date().toISOString(),
  };
  projects.push(newProject);
  return newProject;
}

export function validateProject(payload: ProjectPayload): boolean {
  return Boolean(payload.name && payload.name.trim().length > 0);
}
