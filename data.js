const publications = [
  {
    title: "Improving Sensitivity Analysis by Synthesizing Randomized Clinical Trials With Limited Overlap",
    authors: "<b>Kuan Jiang</b>, Wenjie Hu, Xinxing Lai, Shu Yang, Xiao-Hua Zhou",
    venue: "Statistics in Medicine, 45(18-19), e70637, 2026",
    links: [
      { text: "DOI", url: "https://doi.org/10.1002/sim.70637" }
    ],
    abstract: "A synthesis sensitivity analysis estimator that incorporates randomized clinical trial data when overlap with observational data is limited.",
    citation: `<pre><code>Jiang K, Hu W, Lai X, Yang S, Zhou X-H. Improving Sensitivity Analysis by Synthesizing Randomized Clinical Trials With Limited Overlap. Statistics in Medicine. 2026;45(18-19):e70637. doi:10.1002/sim.70637.</code></pre>`,
    isNew: false,
    isPreprint: false,
    isSelected: true
  },
  {
    title: "A Practical Analysis Procedure on Generalizing Comparative Effectiveness in the Randomized Clinical Trial to the Real-World Trial-Eligible Population",
    authors: "<b>Kuan Jiang</b>, Xin-Xing Lai, Shu Yang, Ying Gao, Xiao-Hua Zhou",
    venue: "Journal of Biopharmaceutical Statistics, 35(6), 1196-1208, 2025",
    links: [
      { text: "DOI", url: "https://doi.org/10.1080/10543406.2025.2489282" }
    ],
    abstract: "A practical procedure combining trial generalization, augmented inverse probability of sampling weighting, and sensitivity analysis for unmeasured confounding.",
    citation: `<pre><code>Jiang K, Lai X-X, Yang S, Gao Y, Zhou X-H. A practical analysis procedure on generalizing comparative effectiveness in the randomized clinical trial to the real-world trial-eligible population. Journal of Biopharmaceutical Statistics. 2025;35(6):1196-1208. doi:10.1080/10543406.2025.2489282.</code></pre>`,
    isNew: false,
    isPreprint: false,
    isSelected: true
  }
];

// Helper functions to filter publications
const getPreprints = () => publications.filter(pub => pub.isPreprint);
const getSelectedPreprints = () => publications.filter(pub => pub.isPreprint && pub.isSelected);
const getPublications = () => publications.filter(pub => !pub.isPreprint);
const getSelectedPublications = () => publications.filter(pub => !pub.isPreprint && pub.isSelected);
const getAllPublications = () => publications.filter(pub => !pub.isPreprint);

// Legacy variables for backward compatibility
const preprints = getSelectedPreprints();
const selectedPublications = getSelectedPublications();
const fullPublications = getAllPublications();

const projects = [];

// Helper functions to filter projects
const getSelectedProjects = () => projects.filter(project => project.isSelected);
const getAllProjects = () => projects;

const researchExperience = [];

// Teaching Data - Replace with your own teaching experience
const teaching = [];

// Academic Services Data - Replace with your own services
const academicServices = [];

// Talks Data - Replace with your own talks
const talks = [];

// Honors Data - Replace with your own honors and awards
const honors = [];
