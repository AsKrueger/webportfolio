(() => {
    const root = document.documentElement;
    root.classList.add("js");

    // Tema claro/oscuro: respeta el sistema hasta que el usuario elige.
    const themeToggle = document.getElementById("theme-toggle");
    themeToggle?.addEventListener("click", () => {
        const current = root.dataset.theme
            || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
        const next = current === "light" ? "dark" : "light";
        root.dataset.theme = next;
        try { localStorage.setItem("theme", next); } catch (e) { /* almacenamiento no disponible */ }
    });

    // Menú móvil.
    const nav = document.getElementById("site-nav");
    const navToggle = document.getElementById("nav-toggle");
    const openLabel = navToggle?.getAttribute("aria-label");
    const setMenu = (open) => {
        nav.classList.toggle("open", open);
        navToggle.setAttribute("aria-expanded", String(open));
        navToggle.setAttribute("aria-label", open ? navToggle.dataset.labelClose : openLabel);
    };
    navToggle?.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
    nav?.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && nav?.classList.contains("open")) {
            setMenu(false);
            navToggle.focus();
        }
    });

    // Borde de la cabecera al hacer scroll.
    const header = document.querySelector(".site-header");
    const onScroll = () => header?.classList.toggle("scrolled", scrollY > 8);
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    // Escalonado de las líneas del terminal.
    document.querySelectorAll(".terminal .t-line").forEach((line, i) => {
        line.style.setProperty("--i", Math.max(i - 4, 0));
    });

    // Aparición progresiva de bloques.
    const revealables = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        const io = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    io.unobserve(entry.target);
                }
            });
        }, { rootMargin: "0px 0px -8% 0px" });
        revealables.forEach((el) => io.observe(el));
    } else {
        revealables.forEach((el) => el.classList.add("visible"));
    }

    // Enlace activo según la sección visible.
    const links = [...document.querySelectorAll('.site-nav a[href*="#"]')];
    const sections = links
        .map((a) => document.getElementById(a.hash.slice(1)))
        .filter(Boolean);
    if (sections.length && "IntersectionObserver" in window) {
        const spy = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                links.forEach((a) => a.classList.toggle("active", a.hash === `#${entry.target.id}`));
            });
        }, { rootMargin: "-45% 0px -50% 0px" });
        sections.forEach((s) => spy.observe(s));
    }

    // Copiar email.
    document.querySelectorAll("[data-copy]").forEach((btn) => {
        btn.addEventListener("click", async () => {
            const label = btn.textContent;
            try {
                await navigator.clipboard.writeText(btn.dataset.copy);
                btn.textContent = btn.dataset.copied;
            } catch (e) {
                btn.textContent = btn.dataset.copy;
            }
            setTimeout(() => { btn.textContent = label; }, 1800);
        });
    });

    // Imprimir CV.
    document.querySelector("[data-print]")?.addEventListener("click", () => print());

    // Ruta solicitada en la página 404.
    document.querySelectorAll("[data-path]").forEach((el) => {
        el.textContent = location.pathname;
    });
})();
