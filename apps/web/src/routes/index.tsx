import { createFileRoute } from '@tanstack/react-router';
import { useEffect, useState } from 'react';
import { getProjects, createProject, Project } from '../lib/api';

export const Route = createFileRoute('/')({
  component: DashboardComponent,
});

function DashboardComponent() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [name, setName] = useState('');
  const [fps, setFps] = useState(30);
  const [resolution, setResolution] = useState('1920x1080');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const loadProjects = async () => {
    try {
      const data = await getProjects();
      setProjects(data);
    } catch (err) {
      setError('Failed to load projects from API');
    }
  };

  useEffect(() => {
    loadProjects();
  }, []);

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;
    setLoading(true);
    setError('');
    try {
      await createProject({ name, fps, resolution });
      setName('');
      await loadProjects();
    } catch (err) {
      setError('Failed to create project');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <h1>OpenCut Video Editor</h1>
      <p>Modern video editing workspace powered by Bun, Vite, and Elysia.</p>

      {error && <div style={{ color: 'red', marginBottom: '1rem' }}>{error}</div>}

      <div style={{ background: '#f4f4f4', padding: '1.5rem', borderRadius: '8px', marginBottom: '2rem' }}>
        <h3>Create New Project</h3>
        <form onSubmit={handleCreate} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', marginBottom: '0.5rem' }}>Project Name:</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="My Awesome Video"
              style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #ccc' }}
              required
            />
          </div>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <div style={{ flex: 1 }}>
              <label style={{ display: 'block', marginBottom: '0.5rem' }}>FPS:</label>
              <input
                type="number"
                value={fps}
                onChange={(e) => Number(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #ccc' }}
              />
            </div>
            <div style={{ flex: 1 }}>
              <label style={{ display: 'block', marginBottom: '0.5rem' }}>Resolution:</label>
              <select
                value={resolution}
                onChange={(e) => setResolution(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #ccc' }}
              >
                <option value="1920x1080">1920x1080 (FHD)</option>
                <option value="3840x2160">3840x2160 (4K)</option>
                <option value="1280x720">1280x720 (HD)</option>
              </select>
            </div>
          </div>
          <button
            type="submit"
            disabled={loading}
            style={{ background: '#0070f3', color: 'white', padding: '0.75rem', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            {loading ? 'Creating...' : 'Create Project'}
          </button>
        </form>
      </div>

      <div>
        <h3>Your Projects</h3>
        {projects.length === 0 ? (
          <p>No projects found. Create your first project above!</p>
        ) : (
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {projects.map((p, idx) => (
              <li key={idx} style={{ background: '#fff', border: '1px solid #ddd', padding: '1rem', borderRadius: '6px', marginBottom: '0.75rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <strong>{p.name}</strong>
                  <div style={{ fontSize: '0.85rem', color: '#666', marginTop: '0.25rem' }}>
                    Resolution: {p.resolution || '1920x1080'} | FPS: {p.fps || 30}
                  </div>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
