title: Publishing PowerPoint presentations with animations as PDFs
date: 2025-04-30 12:00
category: PowerPoint, PDF
tags: PowerPoint, PDF

When I create PowerPoint presentations, I often use animations to explain complex processes. I design slides so the final state is clear on its own, but sometimes this isn’t feasible. When sharing these presentations as PDFs, animations are lost, making slides hard to understand.

I’ve found a solution: [PPSplit](https://github.com/maxonthegit/PPspliT), a PowerPoint plug-in that exports presentations with animations as PDFs. PPSpit works by splitting animated slides into multiple PDF pages, each representing a step in the animation sequence. This preserves the flow and context of the presentation, ensuring viewers can follow the intended progression without needing the original PowerPoint file.

To use PPSpit in Windows, install the plug-in from its [web page](https://www.maxonthenet.altervista.org/ppsplit.php) and open your presentation in PowerPoint. PPsplit will add a new tab to split the slides. Notice that *this changes the file*, so make a copy of the original presentation before using it, especially if you have auto-save enabled. After splitting, you can save the presentation as a PDF. The resulting PDF will have each animation step on a separate page, making it easy to follow along.
