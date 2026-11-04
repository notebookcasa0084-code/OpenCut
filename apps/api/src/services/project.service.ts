export interface ProjectPayload {
  name: string;
  fps?: number;
  resolution?: string;
}

export function validateProject(payload: ProjectPayload): boolean {
  return Boolean(payload.name && payload.name.trim().length > 0);
}
