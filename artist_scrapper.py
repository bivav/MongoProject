from bs4 import BeautifulSoup
import requests
import wikipedia
import re

html_doc = """
<tr class="chart_data1">
  <td class="cell_pos">1</td>
  <td class="cell_art"><a href="/tt/adele.htm">Adele</a></td>
  <td class="cell_dat"><a href="/sm/2008jan.htm">Jan 2008</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">2</td>
  <td class="cell_art"><a href="/tt/eminem.htm">Eminem</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">3</td>
  <td class="cell_art"><a href="/tt/ed_sheeran.htm">Ed Sheeran</a></td>
  <td class="cell_dat"><a href="/sm/2011jun.htm">Jun 2011</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">4</td>
  <td class="cell_art"><a href="/tt/coldplay.htm">Coldplay</a></td>
  <td class="cell_dat"><a href="/sm/2000mar.htm">Mar 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">5</td>
  <td class="cell_art"><a href="/tt/amy_winehouse.htm">Amy Winehouse</a></td>
  <td class="cell_dat"><a href="/sm/2003oct.htm">Oct 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">6</td>
  <td class="cell_art"><a href="/tt/bruno_mars.htm">Bruno Mars</a></td>
  <td class="cell_dat"><a href="/sm/2010feb.htm">Feb 2010</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">7</td>
  <td class="cell_art"><a href="/tt/pink.htm">Pink</a></td>
  <td class="cell_dat"><a href="/sm/2000mar.htm">Mar 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">8</td>
  <td class="cell_art"><a href="/tt/taylor_swift.htm">Taylor Swift</a></td>
  <td class="cell_dat"><a href="/sm/2006sep.htm">Sep 2006</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">9</td>
  <td class="cell_art"><a href="/tt/rihanna.htm">Rihanna</a></td>
  <td class="cell_dat"><a href="/sm/2005jun.htm">Jun 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">10</td>
  <td class="cell_art"><a href="/tt/the_black_eyed_peas.htm">The Black Eyed Peas</a></td>
  <td class="cell_dat"><a href="/sm/2001mar.htm">Mar 2001</a></td>
  <td class="cell_dat"><a href="/am/2013mar.htm">Mar 2013</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">11</td>
  <td class="cell_art"><a href="/tt/guns_n_roses.htm">Guns n' Roses</a></td>
  <td class="cell_dat"><a href="/sm/2008feb.htm">Feb 2008</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">12</td>
  <td class="cell_art"><a href="/tt/linkin_park.htm">Linkin Park</a></td>
  <td class="cell_dat"><a href="/sm/2001jan.htm">Jan 2001</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">13</td>
  <td class="cell_art"><a href="/tt/norah_jones.htm">Norah Jones</a></td>
  <td class="cell_dat"><a href="/sm/2002may.htm">May 2002</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">14</td>
  <td class="cell_art"><a href="/tt/imagine_dragons.htm">Imagine Dragons</a></td>
  <td class="cell_dat"><a href="/sm/2012jun.htm">Jun 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">15</td>
  <td class="cell_art"><a href="/tt/the_beatles.htm">The Beatles</a></td>
  <td class="cell_dat"><a href="/sm/2007dec.htm">Dec 2007</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">16</td>
  <td class="cell_art"><a href="/tt/lady_gaga.htm">Lady GaGa</a></td>
  <td class="cell_dat"><a href="/sm/2008jun.htm">Jun 2008</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">17</td>
  <td class="cell_art"><a href="/tt/michael_jackson.htm">Michael Jackson</a></td>
  <td class="cell_dat"><a href="/sm/2001sep.htm">Sep 2001</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">18</td>
  <td class="cell_art"><a href="/tt/beyonce.htm">Beyonce</a></td>
  <td class="cell_dat"><a href="/sm/2002jul.htm">Jul 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">19</td>
  <td class="cell_art"><a href="/tt/drake.htm">Drake</a></td>
  <td class="cell_dat"><a href="/sm/2006sep.htm">Sep 2006</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">20</td>
  <td class="cell_art"><a href="/tt/maroon_5.htm">Maroon 5</a></td>
  <td class="cell_dat"><a href="/sm/2003aug.htm">Aug 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">21</td>
  <td class="cell_art"><a href="/tt/michael_buble.htm">Michael Buble</a></td>
  <td class="cell_dat"><a href="/sm/2003dec.htm">Dec 2003</a></td>
  <td class="cell_dat"><a href="/am/2018jan.htm">Jan 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">22</td>
  <td class="cell_art"><a href="/tt/bob_marley.htm">Bob Marley</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">23</td>
  <td class="cell_art"><a href="/tt/red_hot_chili_peppers.htm">Red Hot Chili Peppers</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">24</td>
  <td class="cell_art"><a href="/tt/nickelback.htm">Nickelback</a></td>
  <td class="cell_dat"><a href="/sm/2001sep.htm">Sep 2001</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">25</td>
  <td class="cell_art"><a href="/tt/katy_perry.htm">Katy Perry</a></td>
  <td class="cell_dat"><a href="/sm/2008may.htm">May 2008</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">26</td>
  <td class="cell_art"><a href="/tt/green_day.htm">Green Day</a></td>
  <td class="cell_dat"><a href="/sm/2000sep.htm">Sep 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">27</td>
  <td class="cell_art"><a href="/tt/sam_smith.htm">Sam Smith</a></td>
  <td class="cell_dat"><a href="/sm/2012oct.htm">Oct 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">28</td>
  <td class="cell_art"><a href="/tt/avril_lavigne.htm">Avril Lavigne</a></td>
  <td class="cell_dat"><a href="/sm/2002jun.htm">Jun 2002</a></td>
  <td class="cell_dat"><a href="/am/2015sep.htm">Sep 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">29</td>
  <td class="cell_art"><a href="/tt/justin_timberlake.htm">Justin Timberlake</a></td>
  <td class="cell_dat"><a href="/sm/2002sep.htm">Sep 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">30</td>
  <td class="cell_art"><a href="/tt/justin_bieber.htm">Justin Bieber</a></td>
  <td class="cell_dat"><a href="/sm/2009jul.htm">Jul 2009</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">31</td>
  <td class="cell_art"><a href="/tt/evanescence.htm">Evanescence</a></td>
  <td class="cell_dat"><a href="/sm/2003mar.htm">Mar 2003</a></td>
  <td class="cell_dat"><a href="/am/2017dec.htm">Dec 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">32</td>
  <td class="cell_art"><a href="/tt/alicia_keys.htm">Alicia Keys</a></td>
  <td class="cell_dat"><a href="/sm/2001jun.htm">Jun 2001</a></td>
  <td class="cell_dat"><a href="/am/2017feb.htm">Feb 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">33</td>
  <td class="cell_art"><a href="/tt/britney_spears.htm">Britney Spears</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">34</td>
  <td class="cell_art"><a href="/tt/lana_del_rey.htm">Lana Del Rey</a></td>
  <td class="cell_dat"><a href="/sm/2011oct.htm">Oct 2011</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">35</td>
  <td class="cell_art"><a href="/tt/usher.htm">Usher</a></td>
  <td class="cell_dat"><a href="/sm/2000nov.htm">Nov 2000</a></td>
  <td class="cell_dat"><a href="/am/2017may.htm">May 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">36</td>
  <td class="cell_art"><a href="/tt/50_cent.htm">50 Cent</a></td>
  <td class="cell_dat"><a href="/sm/2002nov.htm">Nov 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">37</td>
  <td class="cell_art"><a href="/tt/james_blunt.htm">James Blunt</a></td>
  <td class="cell_dat"><a href="/sm/2005mar.htm">Mar 2005</a></td>
  <td class="cell_dat"><a href="/am/2017sep.htm">Sep 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">38</td>
  <td class="cell_art"><a href="/tt/dido.htm">Dido</a></td>
  <td class="cell_dat"><a href="/sm/2000aug.htm">Aug 2000</a></td>
  <td class="cell_dat"><a href="/am/2014jan.htm">Jan 2014</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">39</td>
  <td class="cell_art"><a href="/tt/the_killers.htm">The Killers</a></td>
  <td class="cell_dat"><a href="/sm/2004mar.htm">Mar 2004</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">40</td>
  <td class="cell_art"><a href="/tt/madonna.htm">Madonna</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">41</td>
  <td class="cell_art"><a href="/tt/the_weeknd.htm">The Weeknd</a></td>
  <td class="cell_dat"><a href="/sm/2012nov.htm">Nov 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">42</td>
  <td class="cell_art"><a href="/tt/twenty_one_pilots.htm">Twenty One Pilots</a></td>
  <td class="cell_dat"><a href="/sm/2015apr.htm">Apr 2015</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">43</td>
  <td class="cell_art"><a href="/tt/one_direction.htm">One Direction</a></td>
  <td class="cell_dat"><a href="/sm/2011sep.htm">Sep 2011</a></td>
  <td class="cell_dat"><a href="/am/2016oct.htm">Oct 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">44</td>
  <td class="cell_art"><a href="/tt/u2.htm">U2</a></td>
  <td class="cell_dat"><a href="/sm/2000oct.htm">Oct 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">45</td>
  <td class="cell_art"><a href="/tt/shakira.htm">Shakira</a></td>
  <td class="cell_dat"><a href="/sm/2001oct.htm">Oct 2001</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">46</td>
  <td class="cell_art"><a href="/tt/sia.htm">Sia</a></td>
  <td class="cell_dat"><a href="/sm/2000may.htm">May 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">47</td>
  <td class="cell_art"><a href="/tt/queen.htm">Queen</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">48</td>
  <td class="cell_art"><a href="/tt/mumford_sons.htm">Mumford &amp; Sons</a></td>
  <td class="cell_dat"><a href="/sm/2009aug.htm">Aug 2009</a></td>
  <td class="cell_dat"><a href="/am/2017sep.htm">Sep 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">49</td>
  <td class="cell_art"><a href="/tt/nelly_furtado.htm">Nelly Furtado</a></td>
  <td class="cell_dat"><a href="/sm/2001feb.htm">Feb 2001</a></td>
  <td class="cell_dat"><a href="/am/2017apr.htm">Apr 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">50</td>
  <td class="cell_art"><a href="/tt/robbie_williams.htm">Robbie Williams</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">51</td>
  <td class="cell_art"><a href="/tt/destiny_s_child.htm">Destiny's Child</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">52</td>
  <td class="cell_art"><a href="/tt/christina_aguilera.htm">Christina Aguilera</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">53</td>
  <td class="cell_art"><a href="/tt/arctic_monkeys.htm">Arctic Monkeys</a></td>
  <td class="cell_dat"><a href="/sm/2005oct.htm">Oct 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">54</td>
  <td class="cell_art"><a href="/tt/muse.htm">Muse</a></td>
  <td class="cell_dat"><a href="/sm/2000feb.htm">Feb 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">55</td>
  <td class="cell_art"><a href="/tt/kelly_clarkson.htm">Kelly Clarkson</a></td>
  <td class="cell_dat"><a href="/sm/2002sep.htm">Sep 2002</a></td>
  <td class="cell_dat"><a href="/am/2018jun.htm">Jun 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">56</td>
  <td class="cell_art"><a href="/tt/kendrick_lamar.htm">Kendrick Lamar</a></td>
  <td class="cell_dat"><a href="/sm/2012aug.htm">Aug 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">57</td>
  <td class="cell_art"><a href="/tt/jack_johnson.htm">Jack Johnson</a></td>
  <td class="cell_dat"><a href="/sm/2002aug.htm">Aug 2002</a></td>
  <td class="cell_dat"><a href="/am/2017nov.htm">Nov 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">58</td>
  <td class="cell_art"><a href="/tt/shania_twain.htm">Shania Twain</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">59</td>
  <td class="cell_art"><a href="/tt/santana.htm">Santana</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">60</td>
  <td class="cell_art"><a href="/tt/the_pussycat_dolls.htm">The Pussycat Dolls</a></td>
  <td class="cell_dat"><a href="/sm/2005may.htm">May 2005</a></td>
  <td class="cell_dat"><a href="/am/2010jul.htm">Jul 2010</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">61</td>
  <td class="cell_art"><a href="/tt/celine_dion.htm">Celine Dion</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">62</td>
  <td class="cell_art"><a href="/tt/nelly.htm">Nelly</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2013nov.htm">Nov 2013</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">63</td>
  <td class="cell_art"><a href="/tt/jennifer_lopez.htm">Jennifer Lopez</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2014aug.htm">Aug 2014</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">64</td>
  <td class="cell_art"><a href="/tt/fleetwood_mac.htm">Fleetwood Mac</a></td>
  <td class="cell_dat"><a href="/sm/2003mar.htm">Mar 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">find({})
  <td class="cell_pos">65</td>
  <td class="cell_art"><a href="/tt/kings_of_leon.htm">Kings of Leon</a></td>
  <td class="cell_dat"><a href="/sm/2003mar.htm">Mar 2003</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">66</td>
  <td class="cell_art"><a href="/tt/il_divo.htm">Il Divo</a></td>
  <td class="cell_dat"><a href="/sm/2005oct.htm">Oct 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">67</td>
  <td class="cell_art"><a href="/tt/gorillaz.htm">Gorillaz</a></td>
  <td class="cell_dat"><a href="/sm/2001mar.htm">Mar 2001</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">68</td>
  <td class="cell_art"><a href="/tt/shawn_mendes.htm">Shawn Mendes</a></td>
  <td class="cell_dat"><a href="/sm/2014jun.htm">Jun 2014</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">69</td>
  <td class="cell_art"><a href="/tt/kanye_west.htm">Kanye West</a></td>
  <td class="cell_dat"><a href="/sm/2003nov.htm">Nov 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">70</td>
  <td class="cell_art"><a href="/tt/abba.htm">Abba</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">71</td>
  <td class="cell_art"><a href="/tt/luke_bryan.htm">Luke Bryan</a></td>
  <td class="cell_dat"><a href="/sm/2007aug.htm">Aug 2007</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">72</td>
  <td class="cell_art"><a href="/tt/keane.htm">Keane</a></td>
  <td class="cell_dat"><a href="/sm/2004feb.htm">Feb 2004</a></td>
  <td class="cell_dat"><a href="/am/2014nov.htm">Nov 2014</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">73</td>
  <td class="cell_art"><a href="/tt/gwen_stefani.htm">Gwen Stefani</a></td>
  <td class="cell_dat"><a href="/sm/2000dec.htm">Dec 2000</a></td>
  <td class="cell_dat"><a href="/am/2018jan.htm">Jan 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">74</td>
  <td class="cell_art"><a href="/tt/enya.htm">Enya</a></td>
  <td class="cell_dat"><a href="/sm/2000nov.htm">Nov 2000</a></td>
  <td class="cell_dat"><a href="/am/2016may.htm">May 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">75</td>
  <td class="cell_art"><a href="/tt/miley_cyrus.htm">Miley Cyrus</a></td>
  <td class="cell_dat"><a href="/sm/2006aug.htm">Aug 2006</a></td>
  <td class="cell_dat"><a href="/am/2018feb.htm">Feb 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">76</td>
  <td class="cell_art"><a href="/tt/enrique_iglesias.htm">Enrique Iglesias</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2015nov.htm">Nov 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">77</td>
  <td class="cell_art"><a href="/tt/the_foo_fighters.htm">The Foo Fighters</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">78</td>
  <td class="cell_art"><a href="/tt/david_guetta.htm">David Guetta</a></td>
  <td class="cell_dat"><a href="/sm/2001jul.htm">Jul 2001</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">79</td>
  <td class="cell_art"><a href="/tt/dr_dre.htm">Dr Dre</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">80</td>
  <td class="cell_art"><a href="/tt/snow_patrol.htm">Snow Patrol</a></td>
  <td class="cell_dat"><a href="/sm/2000nov.htm">Nov 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">81</td>
  <td class="cell_art"><a href="/tt/sean_paul.htm">Sean Paul</a></td>
  <td class="cell_dat"><a href="/sm/2002may.htm">May 2002</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">82</td>
  <td class="cell_art"><a href="/tt/moby.htm">Moby</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">83</td>
  <td class="cell_art"><a href="/tt/mariah_carey.htm">Mariah Carey</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018jan.htm">Jan 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">84</td>
  <td class="cell_art"><a href="/tt/ariana_grande.htm">Ariana Grande</a></td>
  <td class="cell_dat"><a href="/sm/2013mar.htm">Mar 2013</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">85</td>
  <td class="cell_art"><a href="/tt/josh_groban.htm">Josh Groban</a></td>
  <td class="cell_dat"><a href="/sm/2004mar.htm">Mar 2004</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">86</td>
  <td class="cell_art"><a href="/tt/kenny_chesney.htm">Kenny Chesney</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">87</td>
  <td class="cell_art"><a href="/tt/zac_brown_band.htm">Zac Brown Band</a></td>
  <td class="cell_dat"><a href="/sm/2008oct.htm">Oct 2008</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">88</td>
  <td class="cell_art"><a href="/tt/tim_mcgraw.htm">Tim McGraw</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">89</td>
  <td class="cell_art"><a href="/tt/carrie_underwood.htm">Carrie Underwood</a></td>
  <td class="cell_dat"><a href="/sm/2005jul.htm">Jul 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">90</td>
  <td class="cell_art"><a href="/tt/bon_jovi.htm">Bon Jovi</a></td>
  <td class="cell_dat"><a href="/sm/2000may.htm">May 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">91</td>
  <td class="cell_art"><a href="/tt/akon.htm">Akon</a></td>
  <td class="cell_dat"><a href="/sm/2004jun.htm">Jun 2004</a></td>
  <td class="cell_dat"><a href="/am/2009nov.htm">Nov 2009</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">92</td>
  <td class="cell_art"><a href="/tt/anastacia.htm">Anastacia</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2017nov.htm">Nov 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">93</td>
  <td class="cell_art"><a href="/tt/creed.htm">Creed</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2010aug.htm">Aug 2010</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">94</td>
  <td class="cell_art"><a href="/tt/outkast.htm">OutKast</a></td>
  <td class="cell_dat"><a href="/sm/2000nov.htm">Nov 2000</a></td>
  <td class="cell_dat"><a href="/am/2006nov.htm">Nov 2006</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">95</td>
  <td class="cell_art"><a href="/tt/jason_mraz.htm">Jason Mraz</a></td>
  <td class="cell_dat"><a href="/sm/2003may.htm">May 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">96</td>
  <td class="cell_art"><a href="/tt/journey.htm">Journey</a></td>
  <td class="cell_dat"><a href="/sm/2007nov.htm">Nov 2007</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">97</td>
  <td class="cell_art"><a href="/tt/the_black_keys.htm">The Black Keys</a></td>
  <td class="cell_dat"><a href="/sm/2003jun.htm">Jun 2003</a></td>
  <td class="cell_dat"><a href="/am/2015mar.htm">Mar 2015</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">98</td>
  <td class="cell_art"><a href="/tt/limp_bizkit.htm">Limp Bizkit</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2011aug.htm">Aug 2011</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">99</td>
  <td class="cell_art"><a href="/tt/mika.htm">Mika</a></td>
  <td class="cell_dat"><a href="/sm/2007jan.htm">Jan 2007</a></td>
  <td class="cell_dat"><a href="/am/2016aug.htm">Aug 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">100</td>
  <td class="cell_art"><a href="/tt/mary_j_blige.htm">Mary J Blige</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">101</td>
  <td class="cell_art"><a href="/tt/rascal_flatts.htm">Rascal Flatts</a></td>
  <td class="cell_dat"><a href="/sm/2000may.htm">May 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">102</td>
  <td class="cell_art"><a href="/tt/nirvana.htm">Nirvana</a></td>
  <td class="cell_dat"><a href="/sm/2002oct.htm">Oct 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">103</td>
  <td class="cell_art"><a href="/tt/daft_punk.htm">Daft Punk</a></td>
  <td class="cell_dat"><a href="/sm/2000nov.htm">Nov 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">104</td>
  <td class="cell_art"><a href="/tt/florida_georgia_line.htm">Florida Georgia Line</a></td>
  <td class="cell_dat"><a href="/sm/2012sep.htm">Sep 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">105</td>
  <td class="cell_art"><a href="/tt/kid_rock.htm">Kid Rock</a></td>
  <td class="cell_dat"><a href="/sm/2000feb.htm">Feb 2000</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">106</td>
  <td class="cell_art"><a href="/tt/toby_keith.htm">Toby Keith</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017oct.htm">Oct 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">107</td>
  <td class="cell_art"><a href="/tt/fall_out_boy.htm">Fall Out Boy</a></td>
  <td class="cell_dat"><a href="/sm/2005jul.htm">Jul 2005</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">108</td>
  <td class="cell_art"><a href="/tt/meghan_trainor.htm">Meghan Trainor</a></td>
  <td class="cell_dat"><a href="/sm/2014jul.htm">Jul 2014</a></td>
  <td class="cell_dat"><a href="/am/2017jun.htm">Jun 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">109</td>
  <td class="cell_art"><a href="/tt/john_legend.htm">John Legend</a></td>
  <td class="cell_dat"><a href="/sm/2004may.htm">May 2004</a></td>
  <td class="cell_dat"><a href="/am/2017oct.htm">Oct 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">110</td>
  <td class="cell_art"><a href="/tt/leona_lewis.htm">Leona Lewis</a></td>
  <td class="cell_dat"><a href="/sm/2006dec.htm">Dec 2006</a></td>
  <td class="cell_dat"><a href="/am/2015oct.htm">Oct 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">111</td>
  <td class="cell_art"><a href="/tt/duffy.htm">Duffy</a></td>
  <td class="cell_dat"><a href="/sm/2008jan.htm">Jan 2008</a></td>
  <td class="cell_dat"><a href="/am/2011may.htm">May 2011</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">112</td>
  <td class="cell_art"><a href="/tt/onerepublic.htm">OneRepublic</a></td>
  <td class="cell_dat"><a href="/sm/2007apr.htm">Apr 2007</a></td>
  <td class="cell_dat"><a href="/am/2017jan.htm">Jan 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">113</td>
  <td class="cell_art"><a href="/tt/keith_urban.htm">Keith Urban</a></td>
  <td class="cell_dat"><a href="/sm/2000jul.htm">Jul 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">114</td>
  <td class="cell_art"><a href="/tt/chris_stapleton.htm">Chris Stapleton</a></td>
  <td class="cell_dat"><a href="/sm/2015nov.htm">Nov 2015</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">115</td>
  <td class="cell_art"><a href="/tt/shaggy.htm">Shaggy</a></td>
  <td class="cell_dat"><a href="/sm/2000jun.htm">Jun 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">116</td>
  <td class="cell_art"><a href="/tt/eagles.htm">Eagles</a></td>
  <td class="cell_dat"><a href="/sm/2003aug.htm">Aug 2003</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">117</td>
  <td class="cell_art"><a href="/tt/johnny_cash.htm">Johnny Cash</a></td>
  <td class="cell_dat"><a href="/sm/2003may.htm">May 2003</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">118</td>
  <td class="cell_art"><a href="/tt/three_doors_down.htm">Three Doors Down</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2017feb.htm">Feb 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">119</td>
  <td class="cell_art"><a href="/tt/macklemore_ryan_lewis.htm">Macklemore &amp; Ryan Lewis</a></td>
  <td class="cell_dat"><a href="/sm/2012sep.htm">Sep 2012</a></td>
  <td class="cell_dat"><a href="/am/2017oct.htm">Oct 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">120</td>
  <td class="cell_art"><a href="/tt/hozier.htm">Hozier</a></td>
  <td class="cell_dat"><a href="/sm/2014jul.htm">Jul 2014</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">121</td>
  <td class="cell_art"><a href="/tt/the_lumineers.htm">The Lumineers</a></td>
  <td class="cell_dat"><a href="/sm/2012jun.htm">Jun 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">122</td>
  <td class="cell_art"><a href="/tt/sam_hunt.htm">Sam Hunt</a></td>
  <td class="cell_dat"><a href="/sm/2014jul.htm">Jul 2014</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">123</td>
  <td class="cell_art"><a href="/tt/craig_david.htm">Craig David</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">124</td>
  <td class="cell_art"><a href="/tt/chris_brown.htm">Chris Brown</a></td>
  <td class="cell_dat"><a href="/sm/2005aug.htm">Aug 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">125</td>
  <td class="cell_art"><a href="/tt/lady_antebellum.htm">Lady Antebellum</a></td>
  <td class="cell_dat"><a href="/sm/2008mar.htm">Mar 2008</a></td>
  <td class="cell_dat"><a href="/am/2017sep.htm">Sep 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">126</td>
  <td class="cell_art"><a href="/tt/led_zeppelin.htm">Led Zeppelin</a></td>
  <td class="cell_dat"><a href="/sm/2007nov.htm">Nov 2007</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">127</td>
  <td class="cell_art"><a href="/tt/lenny_kravitz.htm">Lenny Kravitz</a></td>
  <td class="cell_dat"><a href="/sm/2000mar.htm">Mar 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">128</td>
  <td class="cell_art"><a href="/tt/metallica.htm">Metallica</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">129</td>
  <td class="cell_art"><a href="/tt/lmfao.htm">LMFAO</a></td>
  <td class="cell_dat"><a href="/sm/2009mar.htm">Mar 2009</a></td>
  <td class="cell_dat"><a href="/am/2013jan.htm">Jan 2013</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">130</td>
  <td class="cell_art"><a href="/tt/elvis_presley.htm">Elvis Presley</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">131</td>
  <td class="cell_art"><a href="/tt/the_dixie_chicks.htm">The Dixie Chicks</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017sep.htm">Sep 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">132</td>
  <td class="cell_art"><a href="/tt/system_of_a_down.htm">System of A Down</a></td>
  <td class="cell_dat"><a href="/sm/2001oct.htm">Oct 2001</a></td>
  <td class="cell_dat"><a href="/am/2015nov.htm">Nov 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">133</td>
  <td class="cell_art"><a href="/tt/kylie_minogue.htm">Kylie Minogue</a></td>
  <td class="cell_dat"><a href="/sm/2000jun.htm">Jun 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">134</td>
  <td class="cell_art"><a href="/tt/john_mayer.htm">John Mayer</a></td>
  <td class="cell_dat"><a href="/sm/2002jun.htm">Jun 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">135</td>
  <td class="cell_art"><a href="/tt/ac_dc.htm">AC/DC</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">136</td>
  <td class="cell_art"><a href="/tt/whitney_houston.htm">Whitney Houston</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">137</td>
  <td class="cell_art"><a href="/tt/florence_the_machine.htm">Florence + The Machine</a></td>
  <td class="cell_dat"><a href="/sm/2008aug.htm">Aug 2008</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">138</td>
  <td class="cell_art"><a href="/tt/r_kelly.htm">R Kelly</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2016dec.htm">Dec 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">139</td>
  <td class="cell_art"><a href="/tt/blake_shelton.htm">Blake Shelton</a></td>
  <td class="cell_dat"><a href="/sm/2001may.htm">May 2001</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">140</td>
  <td class="cell_art"><a href="/tt/alan_jackson.htm">Alan Jackson</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">141</td>
  <td class="cell_art"><a href="/tt/train.htm">Train</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jun.htm">Jun 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">142</td>
  <td class="cell_art"><a href="/tt/pharrell_williams.htm">Pharrell Williams</a></td>
  <td class="cell_dat"><a href="/sm/2002mar.htm">Mar 2002</a></td>
  <td class="cell_dat"><a href="/am/2015sep.htm">Sep 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">143</td>
  <td class="cell_art"><a href="/tt/jason_aldean.htm">Jason Aldean</a></td>
  <td class="cell_dat"><a href="/sm/2005aug.htm">Aug 2005</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">144</td>
  <td class="cell_art"><a href="/tt/katie_melua.htm">Katie Melua</a></td>
  <td class="cell_dat"><a href="/sm/2003dec.htm">Dec 2003</a></td>
  <td class="cell_dat"><a href="/am/2017dec.htm">Dec 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">145</td>
  <td class="cell_art"><a href="/tt/the_white_stripes.htm">The White Stripes</a></td>
  <td class="cell_dat"><a href="/sm/2001nov.htm">Nov 2001</a></td>
  <td class="cell_dat"><a href="/am/2012jul.htm">Jul 2012</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">146</td>
  <td class="cell_art"><a href="/tt/rod_stewart.htm">Rod Stewart</a></td>
  <td class="cell_dat"><a href="/sm/2001mar.htm">Mar 2001</a></td>
  <td class="cell_dat"><a href="/am/2018may.htm">May 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">147</td>
  <td class="cell_art"><a href="/tt/j_cole.htm">J Cole</a></td>
  <td class="cell_dat"><a href="/sm/2010jun.htm">Jun 2010</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">148</td>
  <td class="cell_art"><a href="/tt/n_sync.htm">N Sync</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018jan.htm">Jan 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">149</td>
  <td class="cell_art"><a href="/tt/fergie.htm">Fergie</a></td>
  <td class="cell_dat"><a href="/sm/2000sep.htm">Sep 2000</a></td>
  <td class="cell_dat"><a href="/am/2017oct.htm">Oct 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">150</td>
  <td class="cell_art"><a href="/tt/elton_john.htm">Elton John</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">151</td>
  <td class="cell_art"><a href="/tt/avicii.htm">Avicii</a></td>
  <td class="cell_dat"><a href="/sm/2010aug.htm">Aug 2010</a></td>
  <td class="cell_dat"><a href="/am/2018jun.htm">Jun 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">152</td>
  <td class="cell_art"><a href="/tt/faith_hill.htm">Faith Hill</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018mar.htm">Mar 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">153</td>
  <td class="cell_art"><a href="/tt/blink_182.htm">blink-182</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017jun.htm">Jun 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">154</td>
  <td class="cell_art"><a href="/tt/andrea_bocelli.htm">Andrea Bocelli</a></td>
  <td class="cell_dat"><a href="/sm/2000jun.htm">Jun 2000</a></td>
  <td class="cell_dat"><a href="/am/2016dec.htm">Dec 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">155</td>
  <td class="cell_art"><a href="/tt/bruce_springsteen.htm">Bruce Springsteen</a></td>
  <td class="cell_dat"><a href="/sm/2002jul.htm">Jul 2002</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">156</td>
  <td class="cell_art"><a href="/tt/post_malone.htm">Post Malone</a></td>
  <td class="cell_dat"><a href="/sm/2015sep.htm">Sep 2015</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">157</td>
  <td class="cell_art"><a href="/tt/jay_z.htm">Jay-Z</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018feb.htm">Feb 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">158</td>
  <td class="cell_art"><a href="/tt/the_corrs.htm">The Corrs</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018feb.htm">Feb 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">159</td>
  <td class="cell_art"><a href="/tt/daughtry.htm">Daughtry</a></td>
  <td class="cell_dat"><a href="/sm/2006dec.htm">Dec 2006</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">160</td>
  <td class="cell_art"><a href="/tt/nicki_minaj.htm">Nicki Minaj</a></td>
  <td class="cell_dat"><a href="/sm/2010mar.htm">Mar 2010</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">161</td>
  <td class="cell_art"><a href="/tt/david_gray.htm">David Gray</a></td>
  <td class="cell_dat"><a href="/sm/2000jun.htm">Jun 2000</a></td>
  <td class="cell_dat"><a href="/am/2016nov.htm">Nov 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">162</td>
  <td class="cell_art"><a href="/tt/joss_stone.htm">Joss Stone</a></td>
  <td class="cell_dat"><a href="/sm/2004feb.htm">Feb 2004</a></td>
  <td class="cell_dat"><a href="/am/2015oct.htm">Oct 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">163</td>
  <td class="cell_art"><a href="/tt/franz_ferdinand.htm">Franz Ferdinand</a></td>
  <td class="cell_dat"><a href="/sm/2003sep.htm">Sep 2003</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">164</td>
  <td class="cell_art"><a href="/tt/lorde.htm">Lorde</a></td>
  <td class="cell_dat"><a href="/sm/2013apr.htm">Apr 2013</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">165</td>
  <td class="cell_art"><a href="/tt/kt_tunstall.htm">KT Tunstall</a></td>
  <td class="cell_dat"><a href="/sm/2005feb.htm">Feb 2005</a></td>
  <td class="cell_dat"><a href="/am/2016oct.htm">Oct 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">166</td>
  <td class="cell_art"><a href="/tt/diana_krall.htm">Diana Krall</a></td>
  <td class="cell_dat"><a href="/sm/2004may.htm">May 2004</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">167</td>
  <td class="cell_art"><a href="/tt/pink_floyd.htm">Pink Floyd</a></td>
  <td class="cell_dat"><a href="/sm/2012mar.htm">Mar 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">168</td>
  <td class="cell_art"><a href="/tt/ellie_goulding.htm">Ellie Goulding</a></td>
  <td class="cell_dat"><a href="/sm/2009nov.htm">Nov 2009</a></td>
  <td class="cell_dat"><a href="/am/2016oct.htm">Oct 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">169</td>
  <td class="cell_art"><a href="/tt/david_bowie.htm">David Bowie</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">170</td>
  <td class="cell_art"><a href="/tt/the_fray.htm">The Fray</a></td>
  <td class="cell_dat"><a href="/sm/2006feb.htm">Feb 2006</a></td>
  <td class="cell_dat"><a href="/am/2016dec.htm">Dec 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">171</td>
  <td class="cell_art"><a href="/tt/ray_charles.htm">Ray Charles</a></td>
  <td class="cell_dat"><a href="/sm/2004dec.htm">Dec 2004</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">172</td>
  <td class="cell_art"><a href="/tt/disturbed.htm">Disturbed</a></td>
  <td class="cell_dat"><a href="/sm/2001apr.htm">Apr 2001</a></td>
  <td class="cell_dat"><a href="/am/2017may.htm">May 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">173</td>
  <td class="cell_art"><a href="/tt/matchbox_twenty.htm">Matchbox Twenty</a></td>
  <td class="cell_dat"><a href="/sm/2000apr.htm">Apr 2000</a></td>
  <td class="cell_dat"><a href="/am/2016oct.htm">Oct 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">174</td>
  <td class="cell_art"><a href="/tt/hilary_duff.htm">Hilary Duff</a></td>
  <td class="cell_dat"><a href="/sm/2003jun.htm">Jun 2003</a></td>
  <td class="cell_dat"><a href="/am/2015jul.htm">Jul 2015</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">175</td>
  <td class="cell_art"><a href="/tt/panic_at_the_disco.htm">Panic! At the Disco</a></td>
  <td class="cell_dat"><a href="/sm/2006mar.htm">Mar 2006</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">176</td>
  <td class="cell_art"><a href="/tt/lil_wayne.htm">Lil' Wayne</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">177</td>
  <td class="cell_art"><a href="/tt/good_charlotte.htm">Good Charlotte</a></td>
  <td class="cell_dat"><a href="/sm/2002sep.htm">Sep 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">178</td>
  <td class="cell_art"><a href="/tt/sting.htm">Sting</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2018aug.htm">Aug 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">179</td>
  <td class="cell_art"><a href="/tt/paolo_nutini.htm">Paolo Nutini</a></td>
  <td class="cell_dat"><a href="/sm/2006jul.htm">Jul 2006</a></td>
  <td class="cell_dat"><a href="/am/2016jul.htm">Jul 2016</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">180</td>
  <td class="cell_art"><a href="/tt/sheryl_crow.htm">Sheryl Crow</a></td>
  <td class="cell_dat"><a href="/sm/2002apr.htm">Apr 2002</a></td>
  <td class="cell_dat"><a href="/am/2017jun.htm">Jun 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">181</td>
  <td class="cell_art"><a href="/tt/fun.htm">fun.</a></td>
  <td class="cell_dat"><a href="/sm/2005oct.htm">Oct 2005</a></td>
  <td class="cell_dat"><a href="/am/2014feb.htm">Feb 2014</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">182</td>
  <td class="cell_art"><a href="/tt/creedence_clearwater_revival.htm">Creedence Clearwater 
  Revival</a></td>
  <td class="cell_dat"><a href="/sm/2013mar.htm">Mar 2013</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">183</td>
  <td class="cell_art"><a href="/tt/the_rolling_stones.htm">The Rolling Stones</a></td>
  <td class="cell_dat"><a href="/sm/2002oct.htm">Oct 2002</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">184</td>
  <td class="cell_art"><a href="/tt/staind.htm">Staind</a></td>
  <td class="cell_dat"><a href="/sm/2001apr.htm">Apr 2001</a></td>
  <td class="cell_dat"><a href="/am/2012aug.htm">Aug 2012</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">185</td>
  <td class="cell_art"><a href="/tt/ja_rule.htm">Ja Rule</a></td>
  <td class="cell_dat"><a href="/sm/2000sep.htm">Sep 2000</a></td>
  <td class="cell_dat"><a href="/am/2012mar.htm">Mar 2012</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">186</td>
  <td class="cell_art"><a href="/tt/aaliyah.htm">Aaliyah</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2005aug.htm">Aug 2005</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">187</td>
  <td class="cell_art"><a href="/tt/ke_ha.htm">Ke$ha</a></td>
  <td class="cell_dat"><a href="/sm/2009oct.htm">Oct 2009</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">188</td>
  <td class="cell_art"><a href="/tt/corinne_bailey_rae.htm">Corinne Bailey Rae</a></td>
  <td class="cell_dat"><a href="/sm/2005apr.htm">Apr 2005</a></td>
  <td class="cell_dat"><a href="/am/2016jun.htm">Jun 2016</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">189</td>
  <td class="cell_art"><a href="/tt/ashanti.htm">Ashanti</a></td>
  <td class="cell_dat"><a href="/sm/2001nov.htm">Nov 2001</a></td>
  <td class="cell_dat"><a href="/am/2014apr.htm">Apr 2014</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">190</td>
  <td class="cell_art"><a href="/tt/charlie_puth.htm">Charlie Puth</a></td>
  <td class="cell_dat"><a href="/sm/2015mar.htm">Mar 2015</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">191</td>
  <td class="cell_art"><a href="/tt/passenger.htm">Passenger</a></td>
  <td class="cell_dat"><a href="/sm/2012oct.htm">Oct 2012</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">192</td>
  <td class="cell_art"><a href="/tt/brad_paisley.htm">Brad Paisley</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017sep.htm">Sep 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">193</td>
  <td class="cell_art"><a href="/tt/take_that.htm">Take That</a></td>
  <td class="cell_dat"><a href="/sm/2006nov.htm">Nov 2006</a></td>
  <td class="cell_dat"><a href="/am/2017jul.htm">Jul 2017</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">194</td>
  <td class="cell_art"><a href="/tt/the_backstreet_boys.htm">The Backstreet Boys</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2017aug.htm">Aug 2017</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">195</td>
  <td class="cell_art"><a href="/tt/missy_misdemeanor_elliott.htm">Missy 'Misdemeanor' 
  Elliott</a></td>
  <td class="cell_dat"><a href="/sm/2000jan.htm">Jan 2000</a></td>
  <td class="cell_dat"><a href="/am/2015feb.htm">Feb 2015</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">196</td>
  <td class="cell_art"><a href="/tt/oasis.htm">Oasis</a></td>
  <td class="cell_dat"><a href="/sm/2000feb.htm">Feb 2000</a></td>
  <td class="cell_dat"><a href="/am/2018sep.htm">Sep 2018</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">197</td>
  <td class="cell_art"><a href="/tt/ne_yo.htm">Ne-Yo</a></td>
  <td class="cell_dat"><a href="/sm/2005dec.htm">Dec 2005</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">198</td>
  <td class="cell_art"><a href="/tt/no_doubt.htm">No Doubt</a></td>
  <td class="cell_dat"><a href="/sm/2000mar.htm">Mar 2000</a></td>
  <td class="cell_dat"><a href="/am/2013feb.htm">Feb 2013</a></td>
</tr>
<tr class="chart_data1">
  <td class="cell_pos">199</td>
  <td class="cell_art"><a href="/tt/lily_allen.htm">Lily Allen</a></td>
  <td class="cell_dat"><a href="/sm/2006jul.htm">Jul 2006</a></td>
  <td class="cell_dat"><a href="/am/2018jul.htm">Jul 2018</a></td>
</tr>
<tr class="chart_data2">
  <td class="cell_pos">200</td>
  <td class="cell_art"><a href="/tt/seal.htm">Seal</a></td>
  <td class="cell_dat"><a href="/sm/2001feb.htm">Feb 2001</a></td>
  <td class="cell_dat"><a href="/am/2018apr.htm">Apr 2018</a></td>
</tr>
"""

from pprint import pprint as pp
from pymongo import MongoClient
from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

client = MongoClient()
db = client.get_database("search_engineDB")

collect = db.get_collection("artist_data")

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

artist_list = []

for i in range(200):
    data = soup.find_all("tr", {"class": re.compile("chart_data.*")})[i] \
        .find_all("td", {"class": "cell_art"})

    for j in data:
        artist_list.append(j.text)

# pp(artist_list)

i = 1
error_list = []
for names in artist_list:

    try:
        wiki_page = wikipedia.page(names)
        dob = wiki_page.summary

        if "born" in dob:
            dob = dob[dob.find("born") + 5:dob.find(")")]
        else:
            dob = None

        arguments = {"keywords": names, "limit": 1, "print_urls": True}
        paths = response.download(arguments)

        image_path = paths[names][0]
        print(image_path[image_path.find("downloads")+ 10 : ])
        print(paths[names][0][paths[names][0].find("downloads")+10:])

        data = {
            "_id": i,
            "Name": wiki_page.title,
            "Summary": wiki_page.summary,
            "Url": wiki_page.url,
            "Image": "/static/downloads" + paths[names][0][paths[names][0].find("downloads") + 9:],
            "Dob": dob
        }

        check = collect.insert_one(data)
        print(check.inserted_id)
        i = i + 1

    except wikipedia.exceptions.DisambiguationError:
        error_list.append(names)
        pp(" ---- " + str(error_list) + " ---- ")
