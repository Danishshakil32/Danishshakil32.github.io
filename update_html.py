import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The new projects HTML
projects_html = """<div class="projects-grid">
                    <!-- Project 1 -->
                    <article class="project-card interactive reveal">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/stol_aircraft.png', 'Biomimetic STOL Aircraft Design')">
                            <picture>
                                <img src="data/projects/stol_aircraft.png" alt="Biomimetic STOL Aircraft Design" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page1_img1.png'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Apr 2026 – May 2026</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">SolidWorks</span>
                            <span class="tech-pill badge">CFD</span>
                            <span class="tech-pill badge">Python</span>
                        </div>
                        <h3 class="project-title heading-card">Biomimetic STOL Aircraft Design</h3>
                        <p class="project-desc body-small">Engineered a biomimetic aerodynamic mechanism inspired by the falcon's alula. Validated through CFD simulations, demonstrating delayed flow separation and improved lift coefficients.</p>
                        <button onclick="openModal('data/projects/stol_aircraft.png', 'Biomimetic STOL Aircraft Design')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 2 -->
                    <article class="project-card interactive reveal" style="animation-delay: 0.1s;">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/helical_gearbox.png', 'Two Stage Helical Gearbox')">
                            <picture>
                                <img src="data/projects/helical_gearbox.png" alt="Two Stage Helical Gearbox" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page2_img1.jpeg'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Jan 2026 – Apr 2026</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">Machine Design</span>
                            <span class="tech-pill badge">Machine Learning</span>
                        </div>
                        <h3 class="project-title heading-card">Two Stage Helical Gearbox with ML</h3>
                        <p class="project-desc body-small">Engineered a complete transmission system and developed a Random Forest ML fault diagnosis model to classify and predict early-stage bearing faults.</p>
                        <button onclick="openModal('data/projects/helical_gearbox.png', 'Two Stage Helical Gearbox')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 3 -->
                    <article class="project-card interactive reveal" style="animation-delay: 0.2s;">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/inductor_design.png', 'Pot Core Inductor Design')">
                            <picture>
                                <img src="data/projects/inductor_design.png" alt="Pot Core Inductor Design" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page3_img1.png'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Jan 2026 – Mar 2026</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">Energy Mgmt</span>
                            <span class="tech-pill badge">Heat Transfer</span>
                        </div>
                        <h3 class="project-title heading-card">Pot Core Inductor Design</h3>
                        <p class="project-desc body-small">Optimized pot core inductors for high-efficiency. Evaluated core and copper losses to maximize Q-factor and managed thermal dissipation.</p>
                        <button onclick="openModal('data/projects/inductor_design.png', 'Pot Core Inductor Design')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 4 -->
                    <article class="project-card interactive reveal">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/fluid_diffusion.png', 'Fluid Diffusion and Mass Transfer')">
                            <picture>
                                <img src="data/projects/fluid_diffusion.png" alt="Fluid Diffusion Analysis" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page4_img1.png'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Dec 2025</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">Fluid Mechanics</span>
                            <span class="tech-pill badge">Thermodynamics</span>
                        </div>
                        <h3 class="project-title heading-card">Fluid Diffusion Analysis</h3>
                        <p class="project-desc body-small">Investigated the physical principles of molecular diffusion. Conducted experiments to observe the effects of thermal gradients and concentration variations.</p>
                        <button onclick="openModal('data/projects/fluid_diffusion.png', 'Fluid Diffusion and Mass Transfer')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 5 -->
                    <article class="project-card interactive reveal" style="animation-delay: 0.1s;">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/aerospace_bracket.png', 'Topology Optimization of an Aerospace Bracket')">
                            <picture>
                                <img src="data/projects/aerospace_bracket.png" alt="Aerospace Bracket" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page3_img3.jpeg'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Dec 2025</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">ANSYS</span>
                            <span class="tech-pill badge">FEA</span>
                            <span class="tech-pill badge">CAD</span>
                        </div>
                        <h3 class="project-title heading-card">Aerospace Bracket Opt.</h3>
                        <p class="project-desc body-small">Executed a topology optimization study to maximize stiffness-to-weight ratio. Redesigned into a highly efficient 3D CAD model achieving significant mass reduction.</p>
                        <button onclick="openModal('data/projects/aerospace_bracket.png', 'Topology Optimization of an Aerospace Bracket')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 6 -->
                    <article class="project-card interactive reveal" style="animation-delay: 0.2s;">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/wire_robot.png', 'Wire Travelling Robot')">
                            <picture>
                                <img src="data/projects/wire_robot.png" alt="Wire Travelling Robot" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page1_img2.png'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Dec 2025</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">Theory of Machines</span>
                            <span class="tech-pill badge">Kinematics</span>
                        </div>
                        <h3 class="project-title heading-card">Wire Travelling Robot</h3>
                        <p class="project-desc body-small">Engineered a specialized wire-traveling robot for dynamic stability. Designed a traction-based drive mechanism to prevent pendulum oscillations.</p>
                        <button onclick="openModal('data/projects/wire_robot.png', 'Wire Travelling Robot')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 7 -->
                    <article class="project-card interactive reveal">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/vbelt_drive.png', 'V-Belt Drive System')">
                            <picture>
                                <img src="data/projects/vbelt_drive.png" alt="V-Belt Drive System" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page2_img2.jpeg'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Dec 2024 – Jan 2025</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">SolidWorks</span>
                            <span class="tech-pill badge">Product Design</span>
                        </div>
                        <h3 class="project-title heading-card">V-Belt Drive System</h3>
                        <p class="project-desc body-small">Engineered a complete mechanical V-belt drive transmission system. Executed analytical calculations and translated into a precise 3D CAD assembly.</p>
                        <button onclick="openModal('data/projects/vbelt_drive.png', 'V-Belt Drive System')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>

                    <!-- Project 8 -->
                    <article class="project-card interactive reveal" style="animation-delay: 0.1s;">
                        <div class="project-image-wrapper cursor-pointer" onclick="openModal('data/projects/jet_turbine.png', 'Thermodynamic Analysis of Jet Engine')">
                            <picture>
                                <img src="data/projects/jet_turbine.png" alt="Jet Gas Turbine Engine" class="project-image" loading="lazy" onerror="this.src='assets/images/projects/page4_img2.png'">
                            </picture>
                        </div>
                        <div class="project-meta">
                            <span class="badge badge-status academic">Academic</span>
                            <span class="badge badge-date">Dec 2024 – Jan 2025</span>
                        </div>
                        <div class="project-tech">
                            <span class="tech-pill badge">Thermodynamics</span>
                            <span class="tech-pill badge">EES</span>
                        </div>
                        <h3 class="project-title heading-card">Jet Gas Turbine Engine</h3>
                        <p class="project-desc body-small">Conducted a comprehensive thermodynamic analysis of a military jet engine using Engineering Equation Solver (EES). Evaluated key operational metrics.</p>
                        <button onclick="openModal('data/projects/jet_turbine.png', 'Thermodynamic Analysis of Jet Engine')" class="btn btn-primary" aria-label="View Details">View Image <i data-lucide="image" style="width: 16px; height: 16px;"></i></button>
                    </article>
                </div>"""

# Replace projects-grid block using regex
content = re.sub(r'<div class="projects-grid">.*?</div>\s*</div>\s*</section>', projects_html + '\n            </div>\n        </section>', content, flags=re.DOTALL)

modal_html = """
    <!-- Project Image Modal -->
    <div id="image-modal" class="modal">
        <span class="modal-close" onclick="closeModal()">&times;</span>
        <div style="display:flex; justify-content:center; align-items:center; height:100%; flex-direction:column; padding: 20px;">
            <img id="modal-img" class="modal-content" src="" alt="Project Image" style="max-height: 70vh; margin-bottom: 20px;">
            <div id="modal-caption" style="color: white; font-size: 1.5rem; text-align: center;"></div>
        </div>
    </div>
"""

content = content.replace('</main>', modal_html + '\n    </main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
