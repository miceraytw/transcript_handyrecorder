# Handy Recorder Wiki Schema

This vault is a mixed personal archive of transcripts created from handy recorder audio.

The source material includes:
- family conversations
- children's performances and practice
- speeches and presentations
- medical / academic talks
- meetings and technical discussions
- occasional placeholders, prompts, or very short low-signal clips

The vault follows a Karpathy-style LLM wiki workflow:
- raw source files at the vault root are immutable
- AI maintains `wiki/`
- every ingest updates source notes, topic pages, `wiki/index.md`, and `log.md`

## Primary goals

1. Turn raw transcripts into concise structured source notes.
2. Separate meaningful content from low-signal or placeholder files.
3. Build cross-linked pages for recurring people, domains, and activity types.
4. Preserve ambiguity when transcripts are incomplete, noisy, or context-poor.

## Folder layout

- `wiki/home.md`: main portal
- `wiki/index.md`: maintained content index
- `wiki/start-here.md`: operating manual and prompts
- `wiki/domains/`: major content domains such as family, speeches, meetings, medical talks, music practice
- `wiki/people/`: recurring named people, children, speakers, or family members
- `wiki/questions/`: reusable question pages when a topic is repeatedly asked
- `wiki/patterns/`: synthesis pages across many transcripts
- `wiki/sources/`: one structured note per ingested raw transcript
- `log.md`: append-only maintenance log

## Editorial rules

- Do not modify, rename, or overwrite raw transcript files.
- Keep a clear line between transcript evidence and inference.
- Prefer short, dense pages over long narrative summaries.
- For personal / family content, preserve privacy and avoid amplifying sensitive details.
- Mark low-confidence files clearly when they are too short, noisy, or only contain a prompt.

## Source note format

```md
# <raw filename stem>

## Source
- Raw file: [[<raw filename stem>]]
- Ingest date: YYYY-MM-DD
- Primary type: family | speech | practice | medical | meeting | other
- Primary topic:
- Secondary topics:
- Confidence: high | medium | low

## One-paragraph summary

## Structured notes
- Situation:
- Main content:
- Notable people or roles:
- Reusable ideas or decisions:
- Follow-up or next-step signals:

## Key entities
- Domains:
- People:
- Topics:

## Wiki links
- Related pages: [[...]]

## Uncertainties
- ...
```

## Topic page format

```md
# <topic>

## Summary

## What repeatedly appears
- ...

## Common links
- [[...]]

## Representative source notes
- [[wiki/sources/...]]

## Uncertainties or edge cases
- ...
```

## Ingest workflow

For every ingest:

1. Read the raw transcript.
2. Create or update the matching `wiki/sources/` note.
3. Update relevant `wiki/domains/`, `wiki/people/`, `wiki/questions/`, or `wiki/patterns/` pages.
4. Update `wiki/index.md` if new pages were added.
5. Append a short entry to `log.md`.

## Re-ingest workflow

If the user says a raw transcript was edited or corrected:

1. Re-read the raw transcript.
2. Rebuild or refresh the matching source note.
3. Update all affected topic pages.
4. Update `wiki/index.md` if needed.
5. Append a `re-ingest` entry to `log.md`.

## Lint workflow

Periodically check for:

- orphan pages
- duplicated pages with different names
- unsupported claims
- pages built from only low-signal sources
- placeholder transcripts that should be marked as low-confidence
- important recurring people or domains that still lack a page

## Initial taxonomy

Start with these high-value hubs:

- domains: 家庭對話, 演講與簡報, 醫療與學術內容, 會議與討論, 音樂練習與表演
- people: abo, 孫時語
- patterns: 錄音品質與低訊號檔案, 個人混合錄音 archive 用法

Evolve the taxonomy only when multiple source notes justify it.
