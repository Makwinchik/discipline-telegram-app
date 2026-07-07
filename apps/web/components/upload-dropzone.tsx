'use client';
import { useState } from 'react';
import { createUploadIntent } from '@/lib/api';
export function UploadDropzone() {
  const [progress, setProgress] = useState(0);
  const [message, setMessage] = useState('Drag & drop a video up to 5 GB');
  async function upload(file: File) {
    setMessage(`Preparing ${file.name}`);
    const intent = await createUploadIntent(file);
    await new Promise<void>((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      xhr.upload.onprogress = (event) => setProgress(Math.round((event.loaded / event.total) * 100));
      xhr.onload = () => resolve();
      xhr.onerror = () => reject(new Error('Upload failed'));
      xhr.open('PUT', intent.upload_url);
      xhr.setRequestHeader('content-type', file.type);
      xhr.send(file);
    });
    setMessage('Uploaded. AI processing can now be queued.');
  }
  return <label className="glass flex min-h-64 cursor-pointer flex-col items-center justify-center rounded-3xl p-8 text-center"><input type="file" accept="video/*" className="hidden" onChange={(e) => e.target.files?.[0] && upload(e.target.files[0])} /><div className="text-2xl font-semibold">Upload long-form video</div><p className="mt-3 text-white/60">{message}</p><div className="mt-6 h-2 w-full max-w-md rounded-full bg-white/10"><div className="h-2 rounded-full bg-violet-500" style={{ width: `${progress}%` }} /></div></label>;
}
