import { UploadDropzone } from '@/components/upload-dropzone';
import { getVideos } from '@/lib/api';
export default async function Dashboard() { const videos = await getVideos(); return <div className="space-y-6"><h1 className="text-3xl font-bold">Dashboard</h1><UploadDropzone /><div className="grid gap-4 md:grid-cols-4">{['Processing queue','Storage usage','Credits remaining','Recent exports'].map((x,i)=><div key={x} className="glass rounded-3xl p-5"><p className="text-white/50">{x}</p><p className="mt-2 text-3xl font-bold">{i===2?'1,240':videos.length}</p></div>)}</div></div>; }
