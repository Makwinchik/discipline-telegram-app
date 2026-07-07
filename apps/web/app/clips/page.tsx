import { ClipCard } from '@/components/clip-card';
import { getVideos } from '@/lib/api';
export default async function Clips() { const videos = await getVideos(); const clips = videos.flatMap((v: any) => v.clips ?? []); return <div><h1 className="mb-6 text-3xl font-bold">Generated Clips</h1><div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">{clips.map((clip: any) => <ClipCard key={clip.id} clip={clip} />)}</div></div>; }
