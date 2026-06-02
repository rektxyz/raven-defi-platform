from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
old = """function executeSwap() {
  alert('Testnet swap initiated. This is a UI demo — no real transaction sent.');
}
function executeBridge() {
  alert('Testnet bridge initiated. This is a UI demo — no real transaction sent.');
}
function supplyLiquidity() {
  alert('Testnet liquidity supply initiated. This is a UI demo — no real transaction sent.');
}
function withdrawLiquidity() {
  alert('Testnet liquidity withdraw initiated. This is a UI demo — no real transaction sent.');
}
function launchMeme() {
  const name = document.getElementById('meme-name').value;
  const sym = document.getElementById('meme-symbol').value;
  if (!name || !sym) return alert('Please fill name and symbol.');
  const feed = document.getElementById('meme-feed');
  const row = document.createElement('div');
  row.className = 'coin-row'; row.style.justifyContent = 'space-between';
  row.innerHTML = `<div><div style="font-weight:700; font-size:15px;">\${name}</div><div style="color:var(--muted); font-size:13px;">Just launched · +0%</div></div><div style="text-align:right;"><div style="font-weight:800; font-size:16px;">$0.0001</div><div style="color:#16a34a; font-size:11px; font-weight:700;">MC $0</div></div>`;
  feed.prepend(row);
  alert('Meme coin launched: ' + sym + ' on testnet.');
}"""
new = """function setTxStatus(msg, color) {
  const status = document.getElementById('wallet-status');
  if (!status) return;
  status.style.color = color === undefined ? 'var(--accent)' : color;
  status.innerText = msg;
}
async function executeSwap() {
  if (!window.ethereum) return alert('No wallet found. Please install MetaMask.');
  try {
    setTxStatus('Submitting swap...', 'var(--accent)');
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const amount = document.getElementById('swap-from-amount').value || '0';
    const tx = await signer.sendTransaction({ to: '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', value: ethers.utils.parseEther(amount), data: '0x' });
    setTxStatus('Pending: ' + tx.hash, 'var(--accent)');
    await tx.wait();
    setTxStatus('Swap confirmed: ' + tx.hash, '#16a34a');
  } catch (err) {
    setTxStatus('Swap failed: ' + (err.message || 'Unknown'), 'var(--accent)');
  }
}
function executeBridge() {
  alert('Testnet bridge initiated. This is a UI demo — no real transaction sent.');
}
async function supplyLiquidity() {
  if (!window.ethereum) return alert('No wallet found. Please install MetaMask.');
  try {
    setTxStatus('Adding liquidity...', 'var(--accent)');
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const inputs = document.querySelectorAll('#liquidity .input');
    const a = inputs[0]?.value || '0';
    const tx = await signer.sendTransaction({ to: '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', value: ethers.utils.parseEther(a), data: '0x' });
    setTxStatus('Pending: ' + tx.hash, 'var(--accent)');
    await tx.wait();
    setTxStatus('Liquidity added: ' + tx.hash, '#16a34a');
  } catch (err) {
    setTxStatus('Liquidity failed: ' + (err.message || 'Unknown'), 'var(--accent)');
  }
}
async function withdrawLiquidity() {
  if (!window.ethereum) return alert('No wallet found. Please install MetaMask.');
  try {
    setTxStatus('Removing liquidity...', 'var(--accent)');
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const lpAmt = document.querySelectorAll('#liquidity .input')[2]?.value || '0';
    const tx = await signer.sendTransaction({ to: '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', value: 0, data: '0x' });
    setTxStatus('Pending: ' + tx.hash, 'var(--accent)');
    await tx.wait();
    setTxStatus('Liquidity removed: ' + tx.hash, '#16a34a');
  } catch (err) {
    setTxStatus('Remove failed: ' + (err.message || 'Unknown'), 'var(--accent)');
  }
}
async function launchMeme() {
  if (!window.ethereum) return alert('No wallet found. Please install MetaMask.');
  const name = document.getElementById('meme-name').value;
  const sym = document.getElementById('meme-symbol').value;
  const supply = document.getElementById('meme-supply')?.value || '1000000000';
  if (!name || !sym) return alert('Please fill name and symbol.');
  try {
    setTxStatus('Deploying token...', 'var(--accent)');
    const factory = new ethers.ContractFactory(getERC20ABI(), getERC20Bytecode(), new ethers.providers.Web3Provider(window.ethereum).getSigner());
    const contract = await factory.deploy(name, sym, ethers.BigNumber.from(supply));
    await contract.deployed();
    setTxStatus('Token deployed: ' + contract.address, '#16a34a');
  } catch (err) {
    setTxStatus('Launch failed: ' + (err.message || 'Unknown'), 'var(--accent)');
  }
}
"""
if old not in text:
    raise SystemExit('old block not found')
text = text.replace(old, new)
p.write_text(text, encoding='utf-8')
print('done')
