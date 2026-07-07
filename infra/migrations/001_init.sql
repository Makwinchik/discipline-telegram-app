CREATE TABLE IF NOT EXISTS videos (
  id UUID PRIMARY KEY,
  owner_id VARCHAR(128) NOT NULL,
  title VARCHAR(255) NOT NULL,
  source_key VARCHAR(512) NOT NULL,
  duration_seconds INTEGER,
  status VARCHAR(32) NOT NULL,
  transcript TEXT,
  analysis JSONB,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS clips (
  id UUID PRIMARY KEY,
  video_id UUID NOT NULL REFERENCES videos(id) ON DELETE CASCADE,
  title VARCHAR(255) NOT NULL,
  topic VARCHAR(160) NOT NULL,
  score DOUBLE PRECISION NOT NULL,
  duration_seconds INTEGER NOT NULL,
  output_key VARCHAR(512),
  captions JSONB,
  hashtags JSONB,
  description TEXT
);
