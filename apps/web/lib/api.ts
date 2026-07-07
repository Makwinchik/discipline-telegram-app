const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';
export async function getVideos() {
  const res = await fetch(`${API_URL}/api/v1/videos`, { cache: 'no-store' });
  if (!res.ok) return [];
  return res.json();
}
export async function createUploadIntent(file: File) {
  const res = await fetch(`${API_URL}/api/v1/uploads/intent`, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ filename: file.name, content_type: file.type, size_bytes: file.size }) });
  if (!res.ok) throw new Error('Unable to create upload');
  return res.json();
}
