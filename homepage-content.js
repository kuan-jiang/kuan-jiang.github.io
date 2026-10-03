/**
 * Loads the homepage biography from editable Markdown.
 */
(async function loadHomepageBiography() {
  const container = document.getElementById('home-bio');
  if (!container) return;

  try {
    const response = await fetch('content/home.md');
    if (!response.ok) throw new Error(`Unable to load biography (${response.status})`);

    const markdown = await response.text();
    if (typeof marked === 'undefined' || typeof marked.parse !== 'function') {
      throw new Error('Markdown renderer is unavailable');
    }

    container.innerHTML = marked.parse(markdown);
  } catch (error) {
    console.error(error);
    container.innerHTML = '<p>Biography is temporarily unavailable.</p>';
  }
})();
