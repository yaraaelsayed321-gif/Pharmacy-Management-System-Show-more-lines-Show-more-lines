document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar');
  const toggle = document.getElementById('sidebarToggle');

  if (toggle && sidebar) {
    toggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      document.body.classList.toggle('sidebar-open');
    });
    document.addEventListener('click', (event) => {
      if (window.innerWidth <= 800 && sidebar.classList.contains('open') && !sidebar.contains(event.target) && event.target !== toggle) {
        sidebar.classList.remove('open');
        document.body.classList.remove('sidebar-open');
      }
    });
  }

  document.querySelectorAll('.nav-link').forEach(link => {
    try {
      const current = new URL(window.location.href);
      const target = new URL(link.href, window.location.origin);
      if (current.pathname === target.pathname) link.classList.add('active');
    } catch (e) {}
  });

  const animated = document.querySelectorAll('.stats-grid > *, .product-grid > *, .module-grid > *, .category-grid > *, .panel, .summary-card, .report-card, .cart-row');
  animated.forEach((el, index) => {
    el.classList.add('reveal');
    el.style.animationDelay = `${Math.min(index * 45, 360)}ms`;
  });

  const hero = document.querySelector('.hero');
  if (hero && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    const visual = hero.querySelector('.hero-visual');
    hero.addEventListener('pointermove', (event) => {
      if (!visual) return;
      const rect = hero.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      visual.style.transform = `translate(${x * 10}px, ${y * 7}px)`;
    });
    hero.addEventListener('pointerleave', () => { if (visual) visual.style.transform = ''; });
  }

  document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('pointerenter', () => card.classList.add('is-hovered'));
    card.addEventListener('pointerleave', () => card.classList.remove('is-hovered'));
  });

  // Premium search shortcut: Cmd/Ctrl + K focuses the global search.
  document.addEventListener('keydown', (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      const input = document.querySelector('.search-mini input');
      if (input) input.focus();
    }
  });

  // Keep quantity controls tactile without changing form behavior.
  document.querySelectorAll('.qty-control button, .btn').forEach(button => {
    button.addEventListener('pointerdown', () => button.classList.add('pressed'));
    button.addEventListener('pointerup', () => button.classList.remove('pressed'));
    button.addEventListener('pointerleave', () => button.classList.remove('pressed'));
  });
});
